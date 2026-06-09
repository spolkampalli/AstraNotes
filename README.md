# AstraNotes

## Overview

AstraNotes is a lightweight note-taking application developed for CSEN 296B: AI-Driven Software Development.

The project demonstrates how AI-assisted software development can be combined with human validation, requirements engineering, architecture design, implementation, testing, and documentation throughout the software development lifecycle.

---

## Features

* Create Notes
* Edit Notes
* Delete Notes
* Search Notes
* Tag Management
* Markdown Formatting
* SQLite Storage
* Encrypted Note Content

---

## Technology Stack

* Python 3
* Flask
* SQLite
* Markdown
* Cryptography (Fernet)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AstraNotes
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
AstraNotes
├── docs
├── tests
├── src
│   ├── static
│   ├── templates
│   └── app.py
├── requirements.txt
└── README.md
```

---

## AI Usage

AI tools were used to assist with:

* Requirements generation
* Architecture brainstorming
* Documentation support
* UML planning
* Implementation guidance

All generated artifacts and code were reviewed, validated, and refined through human oversight before inclusion in the project.

---

## Security

* Note content is encrypted before storage.
* Encryption keys remain local.
* Sensitive files are excluded using .gitignore.

---

## Future Enhancements

* Auto-save support
* Cloud synchronization
* User authentication
* Mobile application support
* Advanced tag filtering

---

## Author

Sravani Polkampalli

CSEN 296B Final Project
