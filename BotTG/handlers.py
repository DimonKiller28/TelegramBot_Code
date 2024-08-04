from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import text
import kb

router = Router()


# start


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name),  reply_markup=kb.menu)

# help


@router.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer(text.help, reply_markup=kb.iexit_kb)


@router.callback_query(F.data == "help")
async def help_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.help, reply_markup=kb.iexit_kb)

# menu


@router.message(Command("menu"))
async def menu_handler(msg: Message):
    await msg.answer(text.menu,  reply_markup=kb.menu)


@router.callback_query(F.data == "menu")
async def menu_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text.menu,  reply_markup=kb.menu)

# else


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
