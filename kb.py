from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="✨ Красота", callback_data="beauty"),
    InlineKeyboardButton(text="🔎 Пройти квест", callback_data="start_quest")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

restart_quest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сначала", callback_data='start_quest')]
])

first_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Йа", callback_data="second_question"),
    InlineKeyboardButton(text="Я", callback_data="second_question")],
    [InlineKeyboardButton(text="Саша", callback_data="second_question"),
    InlineKeyboardButton(text="Че", callback_data="second_question")],
    [InlineKeyboardButton(text="Не я", callback_data="second_question"),
    InlineKeyboardButton(text="Гей", callback_data="wrong_answer")]
])
second_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Негры", callback_data="wrong_answer"),
    InlineKeyboardButton(text="Белый", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Солнце", callback_data="wrong_answer"),
    InlineKeyboardButton(text="Луна", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Звезда", callback_data="wrong_answer"),
    InlineKeyboardButton(text="Метеорит", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Небо", callback_data="wrong_answer"),
    InlineKeyboardButton(text="Газон", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Хромосома", callback_data="third_question"),
    InlineKeyboardButton(text="Курсор", callback_data="wrong_answer")]
])
third_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="СЭККС", callback_data="fourth_question"),
    InlineKeyboardButton(text="Стоны", callback_data="fourth_question")],
    [InlineKeyboardButton(text="Порно", callback_data="fourth_question"),
    InlineKeyboardButton(text="Релакс", callback_data="fourth_question")],
    [InlineKeyboardButton(text="Сериал", callback_data="fourth_question"),
    InlineKeyboardButton(text="Под наркотой", callback_data="fourth_question")],
    [InlineKeyboardButton(text="ЖМЖ", callback_data="fourth_question"),
    InlineKeyboardButton(text="МЖМ", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Мне нужен только ты", callback_data="wrong_answer")]
])
fourth_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="-∞", callback_data="fifth_question"),
    InlineKeyboardButton(text="+∞", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="0", callback_data="wrong_answer"),
    InlineKeyboardButton(text="1", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="Че", callback_data="fifth_question"),
    InlineKeyboardButton(text="Это всё?(", callback_data="fifth_question")]
])
fifth_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👍", callback_data="end_quest"),
    InlineKeyboardButton(text="👎", callback_data="wrong_answer")],
    [InlineKeyboardButton(text="❤️", callback_data="end_quest"),
    InlineKeyboardButton(text="Хочу отсосать этому гению", callback_data="secret_answer")],
    [InlineKeyboardButton(text="Хуйня, не делай больше", callback_data="sad_end_quest")]
])