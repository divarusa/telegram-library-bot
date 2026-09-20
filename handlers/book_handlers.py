from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from fsm.book_states import AddBookState
from db.database import add_book_to_db, get_all_books_from_db

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот для учета каталога книг.\n\n/add_book — добавить книгу\n/books — показать каталог")

@router.message(Command("add_book"))
async def start_add_book(message: Message, state: FSMContext):
    await state.set_state(AddBookState.id)
    await message.answer("Введите номер " \
    "книги (целое число):")

@router.message(AddBookState.id)
async def process_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Номер книги должен быть числом. Попробуйте еще раз:")
        return
    
    await state.update_data(book_id=int(message.text))
    await state.set_state(AddBookState.title)
    await message.answer("Введите название книги:")

@router.message(AddBookState.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddBookState.author)
    await message.answer("Введите автора книги:")

@router.message(AddBookState.author)
async def process_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(AddBookState.genre)
    await message.answer("Введите жанр книги:")

@router.message(AddBookState.genre)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    
    try:
        await add_book_to_db(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            genre=data["genre"]
        )
        summary = (
            "Книга успешно добавлена!\n\n"
            f"ID: {data['book_id']}\n"
            f"Название: {data['title']}\n"
            f"Автор: {data['author']}\n"
            f"Жанр: {data['genre']}"
        )
        await message.answer(summary)
    except Exception:
        await message.answer("Ошибка при сохранении. Возможно, книга с таким ID уже есть.")
    
    await state.clear()

@router.message(Command("books"))
async def cmd_books(message: Message):
    books = await get_all_books_from_db()
    
    if not books:
        await message.answer("База данных пуста.")
        return
    
    for book in books:
        book_id, title, author, genre = book
        await message.answer(
            f"Книга №{book_id}\n"
            f"Название: {title}\n"
            f"Автор: {author}\n"
            f"Жанр: {genre}"
        )