from . import handlers
from . import settings

from aiogram import Router

core_router = Router()

core_router.include_router(handlers.handlers_router)

