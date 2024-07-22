from aiogram import Bot, Dispatcher

import asyncio
import logging
import sys

from core.settings import setting

from core import core_router


async def main():

    bot = Bot(token=setting.bot.bot_token)

    dp = Dispatcher()

    dp.include_router(core_router)

    try:
        await dp.start_polling(bot)
    except asyncio.exceptions.CancelledError:
        pass
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
