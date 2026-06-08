# AstraNotes Class Diagram

```mermaid
classDiagram
    class Note {
        int id
        string title
        string content
        string tags
    }

    class FlaskApp {
        home()
        add_note()
        edit_note()
        delete_note()
    }

    class SQLiteDatabase {
        saveNote()
        loadNotes()
        updateNote()
        deleteNote()
    }

    class EncryptionService {
        encrypt_text()
        decrypt_text()
    }

    class MarkdownRenderer {
        renderMarkdown()
    }

    FlaskApp --> Note
    FlaskApp --> SQLiteDatabase
    FlaskApp --> EncryptionService
    FlaskApp --> MarkdownRenderer