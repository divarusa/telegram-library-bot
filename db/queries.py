CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER UNIQUE NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);
"""

CREATE_TABLE_DETAIL = """
CREATE TABLE IF NOT EXISTS books_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    book_id INTEGER UNIQUE NOT NULL,
    genre TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);
"""

CREATE_TABLE_STARTUP = """
CREATE TABLE IF NOT EXISTS bot_startups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL
);
"""

CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS bot_users (
    chat_id INTEGER PRIMARY KEY,
    updated_at TEXT NOT NULL
);
"""

insert_book = """
INSERT INTO books (book_id, title, author) VALUES (?, ?, ?);
"""

insert_book_detail = """
INSERT INTO books_detail (book_id, genre) VALUES (?, ?);
"""

get_all_books = """
SELECT b.book_id, b.title, b.author, bd.genre
FROM books b
INNER JOIN books_detail bd ON b.book_id = bd.book_id;
"""

insert_startup = """
INSERT INTO bot_startups (started_at) VALUES (?);
"""

save_user = """
INSERT INTO bot_users (chat_id, updated_at) VALUES (?, ?)
ON CONFLICT(chat_id) DO UPDATE SET updated_at = excluded.updated_at;
"""

get_last_chat_id = """
SELECT chat_id FROM bot_users ORDER BY updated_at DESC LIMIT 1;
"""