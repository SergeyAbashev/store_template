from aiogram import Bot, Dispatcher
import asyncio
import logging

from config import TOKEN
from app.database.models import async_main
from app.handlers import router
from app.admin import admin

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(admin, router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
