from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

from time import sleep

import kb, text

router = Router()
beauty_text = open('data/beauty/text.txt', 'r', encoding="utf-8").read().split('-')
photo = FSInputFile("photo.jpg")

second_photo = FSInputFile("Second.png")
end_photo = FSInputFile("end.png")
sad_end_photo = FSInputFile("sad_end.jpg")

@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=f"<b>{msg.from_user.full_name}</b>"), reply_markup=kb.menu)
    
@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "menu")
async def callback_menu(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == 'beauty')
async def beauty(clbck: CallbackQuery):
    await clbck.answer()
    message = await clbck.message.answer(beauty_text[0])
    for i in range(1, len(beauty_text)):
        sleep(0.1)
        await message.edit_text(beauty_text[i])
    await clbck.message.answer_photo(photo, "Nya ❤️")

@router.callback_query(F.data == 'start_quest')
async def start_quest(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.first_question, reply_markup=kb.first_question)

@router.callback_query(F.data == 'second_question')
async def second_question(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer_photo(second_photo, text.second_question, reply_markup=kb.second_question)

@router.callback_query(F.data == "third_question")
async def third_question(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.third_question, reply_markup=kb.third_question)

@router.callback_query(F.data == "fourth_question")
async def fourth_question(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.fourth_question, reply_markup=kb.fourth_question)

@router.callback_query(F.data == "fifth_question")
async def fifth_question(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.fifth_question, reply_markup=kb.fifth_question)

@router.callback_query(F.data == "end_quest")
async def end_quest(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer_photo(end_photo, text.end_quest, reply_markup=kb.iexit_kb)

@router.callback_query(F.data == "sad_end_quest")
async def sad_end_quest(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer_photo(sad_end_photo, text.sad_end_quest, reply_markup=kb.iexit_kb)


@router.callback_query(F.data == 'wrong_answer')
async def wrong_answer(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.wrong_answer, reply_markup=kb.restart_quest)

@router.callback_query(F.data == "secret_answer")
async def secret_answer(clbck: CallbackQuery):
    await clbck.answer()
    await clbck.message.answer(text.secret_answer, reply_markup=kb.iexit_kb)
