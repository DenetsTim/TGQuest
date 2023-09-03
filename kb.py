from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="✨ Красота", callback_data="beauty"),
    InlineKeyboardButton(text="🔎 Пройти квест", callback_data="start_quest")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

first_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Йа", callback_data="second_question"),
    InlineKeyboardButton(text="Я", callback_data="second_question")],
    [InlineKeyboardButton(text="Саша", callback_data="second_question"),
    InlineKeyboardButton(text="Че", callback_data="second_question")],
    [InlineKeyboardButton(text="Не я", callback_data="second_question"),
    InlineKeyboardButton(text="Гей", callback_data="wrong_answer")]
])