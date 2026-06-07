import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = "astranotes.db"


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

    if search_query:
        notes = conn.execute(
            """
            SELECT *
            FROM notes
            WHERE title LIKE ?
            OR content LIKE ?
            OR tags LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{search_query}%",
                f"%{search_query}%",
                f"%{search_query}%"
            )
        ).fetchall()
    else:
        notes = conn.execute(
            "SELECT * FROM notes ORDER BY id DESC"
        ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        notes=notes,
        search_query=search_query
    )


@app.route("/add", methods=["POST"])
def add_note():
    title = request.form["title"]
    content = request.form["content"]
    tags = request.form.get("tags", "")

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)",
        (title, content, tags)
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

        conn.execute(
            """
            UPDATE notes
            SET title = ?, content = ?, tags = ?
            WHERE id = ?
            """,
            (title, content, tags, note_id)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    note = conn.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        note=note
    )


if __name__ == "__main__":
    init_db()
    add_missing_columns()
    app.run(debug=True)