# AstraNotes Object Diagram

```mermaid
classDiagram
    object User
    object Note1 {
        id = 1
        title = "CSEN Project"
        tags = "school,project"
    }

    object Database
    object EncryptionService

    User --> Note1 : creates
    Note1 --> EncryptionService : encrypts content
    EncryptionService --> Database : stores encrypted note
```
