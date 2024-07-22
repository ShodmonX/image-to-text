from aiogram import Bot
from aiogram.types import Message

from core.settings import setting
from core.utils import commands
from core.middlewares import dbbasic
from core.keyboards import inline_keyboard


async def startup_bot(bot: Bot):
    await commands.set_commands(bot=bot)
    await bot.send_message(setting.bot.creator, "Bot ishga tushdi ✅")

async def shutdown_bot(bot: Bot):
    await commands.delete_commands(bot=bot)
    await bot.send_message(setting.bot.creator, "Bot ishdan to'xtadi ❗")


async def start_command(message: Message, bot: Bot):
    if str(message.from_user.id) in dbbasic.all_user_ids():
        await message.reply(f"Assalomu alaykum {message.from_user.first_name}. Xush kelibsiz\n\nMenga rasm yuboring")
        dbbasic.user_condition_change_active(message.from_user.id)
    else:
        await message.answer(f"Assalomu alaykum {message.from_user.first_name}. Xush kelibsiz\n\nMenga matn mavjud bo'lgan biror bir rasm yuboring")
        await bot.send_message(setting.bot.creator, f"NEW USER\n\nFIRST NAME: {message.from_user.first_name}\nLAST NAME: {message.from_user.last_name}\nUSERNAME: {message.from_user.username}\nUSER ID: {message.from_user.id}")
        dbbasic.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)


async def help_command(message: Message):
    await message.reply("Assalomu alaykum, xush kelibsiz\nMen sizga rasmlardan matnlarni ajratib olishda yordam beraman. Iltimos menga tushunarliroq bo'lishi uchun rasmdan matni ajratib olish kerak bo'lgan qismini qirqib jo'nating!\n\nYaratuvchi: @Shodmon_Xolmurodov_bot", reply_markup=inline_keyboard.help_button)
