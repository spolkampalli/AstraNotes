# AstraNotes Testing Notes

## Testing Overview

Testing was performed manually throughout development to verify that implemented features behaved as expected.

## Test Environment

* macOS
* Python 3.13
* Flask
* SQLite
* Google Chrome

## Functional Tests Performed

### Create Note

* Created new notes with title and content.
* Verified notes were saved successfully.

Result: Pass

### Edit Note

* Modified existing note titles, content, and tags.
* Verified updates persisted.

Result: Pass

### Delete Note

* Deleted existing notes.
* Verified notes were removed from the database and UI.

Result: Pass

### Search Notes

* Searched by title keywords.
* Searched by content keywords.
* Searched by tags.

Result: Pass

### Tag Management

* Added multiple tags.
* Verified tag chip display.
* Verified tags remained after editing.

Result: Pass

### Markdown Rendering

* Tested headings, bold text, lists, and blockquotes.
* Verified proper rendering in the note display.

Result: Pass

### Encryption

* Verified note content is encrypted before storage.
* Verified encrypted content is decrypted correctly for display.

Result: Pass

## Issues Encountered

* Initial tag support required database schema updates.
* Markdown rendering required conversion from Markdown to HTML before display.
* Encryption required handling existing unencrypted notes during testing.

## Final Assessment

All planned core functionality was successfully implemented and tested. No critical issues remained at project completion.