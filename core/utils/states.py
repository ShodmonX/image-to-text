from aiogram.fsm.state import StatesGroup, State


class myStates(StatesGroup):
    send_message = State()