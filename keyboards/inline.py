from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="📊 Status", callback_data="status")
    kb.adjust(1)
    return kb.as_markup()

def status():
    kb = InlineKeyboardBuilder()
    kb.button(text="⚡ Enable", callback_data="enable")
    kb.button(text="🔌 Disable", callback_data="disable")
    kb.button(text="♻️ Refresh", callback_data="refresh")
    kb.button(text="📋 Menu", callback_data="menu")
    kb.adjust(3, 1)
    return kb.as_markup()
