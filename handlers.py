from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

from time import sleep

import kb, text

router = Router()
beauty_text = open('data/beauty/text.txt', 'r', encoding="utf-8").read().split('-')
photo = FSInputFile("photo.png")

@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=f"<b>{msg.from_user.full_name}</b>"), reply_markup=kb.menu)
    
@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == 'beauty')
async def beauty(clbck: CallbackQuery):
    message = await clbck.message.answer(beauty_text[0])
    for i in range(1, len(beauty_text)):
        sleep(0.1)
        await message.edit_text(beauty_text[i])
    await clbck.message.answer_photo(photo, "Nya ❤️")

@router.callback_query(F.data == 'start_quest')
async def start_quest(clbck: CallbackQuery):
    await clbck.message.answer(text.first_question, reply_markup=kb.first_question)

@router.callback_query(F.data == 'second_question')
async def second_question(clbck: CallbackQuery):
    await clbck.message.answer("Nice!")

@router.callback_query(F.data == 'wrong_answer')
async def wrong_answer(clbck: CallbackQuery):
    await clbck.message.answer("Неа", reply_markup=kb.exit_kb)
