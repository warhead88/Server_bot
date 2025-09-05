import asyncio

from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.inline import main_menu, status

from services.IPMI import get_power_status, set_power
from services.ping import wait_for_boot
from config import Config

ip = str(Config.SERVER_IP)

router = Router()

@router.message(Command("start"))
async def menu(message: types.Message):
    await message.answer("""This bot lets you manage your server via IPMI.  
You can power it on, shut it down, or check its current status directly from here.  
Choose an option below to get started.""", reply_markup=main_menu())

@router.callback_query(F.data == "menu")
async def ret(callback: types.CallbackQuery):
    await callback.message.edit_text("""This bot lets you manage your server via IPMI.  
You can power it on, shut it down, or check its current status directly from here.  
Choose an option below to get started.""", reply_markup=main_menu())
    await callback.answer()

@router.callback_query(F.data == "status")
async def show_status(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "on":
        stat = "🟢 Active"
        stt = "enabled"
    else:
        stat = "🔴 Inactive"
        stt = "disabled"
    await callback.message.edit_text(f"""📡 Server Status: {stat}

The server is currently {stt}.
Use the menu below to change its state or refresh the status.""", reply_markup=status())
    await callback.answer()

@router.callback_query(F.data == "refresh")
async def refresh(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "on":
        stat = "🟢 Active"
        stt = "enabled"
    else:
        stat = "🔴 Inactive"
        stt = "disabled"
    try:
        await callback.message.edit_text(f"""📡 Server Status: {stat}

The server is currently {stt}.
Use the menu below to change its state or refresh the status.""", reply_markup=status())
    except:
        pass
    await callback.answer()

@router.callback_query(F.data == "enable")
async def turn_on(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "on":
        await callback.answer("Server is already started!")
        return
    await asyncio.to_thread(set_power, "on")
    await callback.message.answer("Server is starting...")
    await callback.answer()
    condition = await asyncio.to_thread(wait_for_boot, ip)
    if condition == True:
        await callback.message.answer("✅ Server has successfully booted into the OS!")
    else:
        await callback.message.answer("Something went wrong.")

@router.callback_query(F.data == "disable")
async def turn_off(callback: types.CallbackQuery):
    state = await asyncio.to_thread(get_power_status)
    if state == "off":
        await callback.answer("Server is already stopped!")
        return
    await asyncio.to_thread(set_power, "off")
    await callback.message.answer("Server is stopping...")
    await callback.answer()
