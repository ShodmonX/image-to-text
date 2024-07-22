from . import basics
from . import admin
from . import getphoto

from aiogram import Router, F
from aiogram.filters import Command

from core.filters import filtersAdmin
from core.utils import states

handlers_router = Router()

handlers_router.startup.register(basics.startup_bot)
handlers_router.shutdown.register(basics.shutdown_bot)

handlers_router.message.register(getphoto.get_photo, F.photo)

handlers_router.message.register(admin.send_message_users, states.myStates.send_message)

handlers_router.message.register(basics.help_command, Command(commands="help"))

handlers_router.message.register(admin.admin_message_answer, filtersAdmin.AdminFilter())

handlers_router.message.register(basics.start_command, Command(commands="start"))

