import asyncio

from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.inline import main_menu, status

from services.IPMI import get_power_status, set_power

router = Router()

@router.message(Command("start"))
async def menu(message: types.Message):
    await message.answer("Basic menu", reply_markup=main_menu())

@router.callback_query(F.data == "menu")
async def ret(callback: types.CallbackQuery):
    await callback.message.edit_text("Basic menu", reply_markup=main_menu())
    await callback.answer()

@router.callback_query(F.data == "status")
async def show_status(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "on":
        stat = "🟢 Active"
    else:
        stat = "🔴 Inactive"
    await callback.message.edit_text(f"Status: {stat}", reply_markup=status())
    await callback.answer()

@router.callback_query(F.data == "refresh")
async def refresh(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "on":
        stat = "🟢 Active"
    else:
        stat = "🔴 Inactive"
    try:
        await callback.message.edit_text(f"Status: {stat}", reply_markup=status())
    except:
        pass
    await callback.answer()

@router.callback_query(F.data == "enable")
async def turn_on(callback: types.CallbackQuery):
    await asyncio.to_thread(set_power, "on")
    await callback.message.answer("Server is starting...")
    await callback.answer()

@router.callback_query(F.data == "disable")
async def turn_off(callback: types.CallbackQuery):
    await asyncio.to_thread(set_power, "off")
    await callback.message.answer("Server is stopping...")
    await callback.answer()
