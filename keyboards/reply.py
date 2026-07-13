from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


def start_keyboard():
    """начинает работу магазина"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='начать 😀')]
        ],
        resize_keyboard=True
    )

def get_main_menu():
    pass