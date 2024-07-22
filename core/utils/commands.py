from aiogram.types import BotCommand
from aiogram import Bot

async def set_commands(bot: Bot):

    commands = [
        BotCommand(
            command="/start",
            description="Botni ishga tushurish"
            ),
        BotCommand(
            command="/help",
            description="Yordam"
        )
    ]

    await bot.set_my_commands(commands=commands)

async def delete_commands(bot: Bot):
    await bot.delete_my_commands()