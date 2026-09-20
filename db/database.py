import aiosqlite
from db import queries
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).resolve().parent.parent / "bot_database.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript(
            queries.CREATE_TABLE
            + queries.CREATE_TABLE_DETAIL
            + queries.CREATE_TABLE_STARTUP
            + queries.CREATE_TABLE_USERS
        )
        await db.commit()

async def record_startup():
    started_at = datetime.now(timezone.utc).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.insert_startup, (started_at,))
        await db.commit()

async def save_user_chat(chat_id: int):
    updated_at = datetime.now(timezone.utc).isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.save_user, (chat_id, updated_at))
        await db.commit()

async def get_last_chat_id():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(queries.get_last_chat_id) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None

async def add_book_to_db(book_id: int, title: str, author: str, genre: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(queries.insert_book, (book_id, title, author))
        await db.execute(queries.insert_book_detail, (book_id, genre))
        await db.commit()

async def get_all_books_from_db():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(queries.get_all_books) as cursor:
            rows = await cursor.fetchall()
            return rows