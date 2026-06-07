import os
import sqlite3
import markdown
from flask import Flask, render_template, request, redirect
from markupsafe import Markup
from cryptography.fernet import Fernet

app = Flask(__name__)

DATABASE = "astranotes.db"
KEY_FILE = "secret.key"


def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


cipher = Fernet(load_or_create_key())


def encrypt_text(text):
    return cipher.encrypt(text.encode()).decode()


def decrypt_text(encrypted_text):
    try:
        return cipher.decrypt(encrypted_text.encode()).decode()
    except Exception:
        return encrypted_text


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_missing_columns():
    conn = get_db_connection()

    try:
        conn.execute("ALTER TABLE notes ADD COLUMN tags TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass

    conn.close()


@app.route("/")
def home():
    search_query = request.args.get("search", "")

    conn = get_db_connection()
    stored_notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()

    processed_notes = []

    for note in stored_notes:
        note_dict = dict(note)

        decrypted_content = decrypt_text(note["content"])
        note_dict["content"] = decrypted_content
        note_dict["html_content"] = Markup(markdown.markdown(decrypted_content))

        if search_query:
            search_target = (
                note_dict["title"] + " " +
                decrypted_content + " " +
                (note_dict["tags"] or "")
            ).lower()

            if search_query.lower() not in search_target:
                continue

        processed_notes.append(note_dict)

    return render_template(
        "index.html",
        notes=processed_notes,
        search_query=search_query
    )


@app.route("/add", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]
    tags = request.form.get("tags", "")

    encrypted_content = encrypt_text(content)

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)",
        (title, encrypted_content, tags)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    conn = get_db_connection()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        tags = request.form.get("tags", "")

        encrypted_content = encrypt_text(content)

        conn.execute(
            """
            UPDATE notes
            SET title = ?, content = ?, tags = ?
            WHERE id = ?
            """,
            (title, encrypted_content, tags, note_id)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    note = conn.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    conn.close()

    note_dict = dict(note)
    note_dict["content"] = decrypt_text(note_dict["content"])

    return render_template(
        "edit.html",
        note=note_dict
    )


if __name__ == "__main__":
    init_db()
    add_missing_columns()
    app.run(debug=True)