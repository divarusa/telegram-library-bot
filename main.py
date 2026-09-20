import asyncio
import logging

from config import bot, dp
from db.database import init_db
from handlers.book_handlers import router as book_router

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    await init_db()
    dp.include_router(book_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())