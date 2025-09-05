from aiogram import Router, types, F
from aiogram.filters import Command
from keyboard.inline import main_menu, status

router = Router()

@router.message(Command("start"))
async def menu(message: types.Message):
    await message.answer("Basic menu", reply_markup=main_menu())

@router.callback_query(F.data="status")
async def show_status(callback: types.CallbackQuery):
    await messahe.edit_text(f"Status: {status}", reply_markup=status())

@router.callback_query(F.data="refresh")
async def refresh(callback: types.CallbackQuery):
    await message.edit_text(f"Status: {status}", reply_markup=status())
