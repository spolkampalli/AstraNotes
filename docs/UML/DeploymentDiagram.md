# AstraNotes Deployment Diagram

```mermaid
flowchart LR
    User[User Browser]

    Flask[Flask Application]

    SQLite[(SQLite Database)]

    Key[Encryption Key]

    User --> Flask
    Flask --> SQLite
    Flask --> Key
```