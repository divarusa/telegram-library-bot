from aiogram.fsm.state import State, StatesGroup

class AddBookState(StatesGroup):
    id = State()
    title = State()
    author = State()
    genre = State()