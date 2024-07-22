from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError


from core.middlewares import dbbasic
from core.keyboards import reply_keyboard
from core.utils import states

async def admin_message_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text == "/start":
        await message.answer("Assalomu alaykum admin", reply_markup=reply_keyboard.buttons_admin)
    elif message.text.lower() == "send message":
        await message.answer("Yubormoqchi bo'lgan xabaringizni kiriting")
        await state.set_state(state=states.myStates.send_message)
    elif message.text.lower() == "users":
        await message.answer(f"ALL USERS: {dbbasic.number_of_all_users()}\nACTIVE USERS: {dbbasic.number_of_active_users()}\nPASSIVE USERS: {dbbasic.number_of_passive_users()}")


async def send_message_users(message: Message, bot: Bot, state: FSMContext):
    for user_id in dbbasic.all_user_ids():
        try:
            await bot.send_message(user_id, message.text)
        except TelegramForbiddenError:
            dbbasic.user_condition_change_passive(user_id=user_id)
    await message.answer("Xabaringiz jo'natildi", reply_markup=reply_keyboard.buttons_admin)
    await state.clear()