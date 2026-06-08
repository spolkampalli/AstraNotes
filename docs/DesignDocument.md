# AstraNotes Design Document

## Architecture Overview

AstraNotes is a Flask-based web application that allows users to create, edit, search, organize, and securely store notes.

## Components

### User Interface

HTML templates and CSS provide the user interface.

### Flask Application

Handles routing, note creation, editing, deletion, searching, and business logic.

### SQLite Database

Stores note titles, encrypted note content, and tags.

### Markdown Renderer

Converts Markdown note content into formatted HTML for display.

### Encryption Service

Uses Fernet encryption to encrypt note content before storage and decrypt it when displayed.

## Main Features

* Create Notes
* Edit Notes
* Delete Notes
* Search Notes
* Tag Management
* Markdown Support
* Encrypted Storage

## Deployment

The application runs locally using:

* Python
* Flask
* SQLite

No external servers or cloud services are required.

## Design Rationale

The architecture prioritizes simplicity, maintainability, privacy, and ease of demonstration while satisfying project requirements.