from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


def start_keyboard():
    """start"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="начать 😀")]
        ],
        resize_keyboard=True
    )