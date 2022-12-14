CREATE TABLE employee
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name  TEXT    NOT NULL,
    first_name TEXT    NOT NULL,
    position   TEXT    NOT NULL,
    salary     INTEGER NOT NULL,
    bonus      INTEGER
)