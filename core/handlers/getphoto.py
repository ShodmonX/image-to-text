from aiogram import Bot
from aiogram.types import Message

from core.imagetotext import imagetotext

import os

async def get_photo(message: Message, bot: Bot):
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "image.png")
    await message.answer(str(imagetotext.imagetotext()))
    if os.path.exists("image.png"):
        os.remove("image.png")

