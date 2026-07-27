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
def phone_button():
    builder = ReplyKeyboardMarkup()
    builder.button(text="Предоставьте номер телефона", request_contact=True)
    return builder.as_markup(resize_keyboard=True)

def get_main_menu():
    """создание основного меню сервиса"""
    builder = ReplyKeyboardBuilder()
    builder.button(text='Сделать заказ 🛎')
    builder.button(text='История 📚')
    builder.button(text='Корзина пользователя 🗑')
    builder.button(text='Настройки ⚙')
    builder.adjust(1,3)
    return builder.as_markup(resize_keyboard=True)

def back_to_main_menu():
    """Возврат в главное меню"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="◀")
    return builder.as_markup(resize_keyboard=True)