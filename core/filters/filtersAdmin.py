from aiogram.types import Message
from aiogram.filters import BaseFilter

from core.settings import setting

class AdminFilter(BaseFilter):
    async def __call__(self, message: Message):
        if str(message.from_user.id) in setting.bot.admin_ids:
            return True
        return False
    
