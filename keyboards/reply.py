from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder


def start_keyboard():
    """начинает работу магазина"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='начать 😀')]
        ],
        resize_keyboard=True
    )
def phone_button():
    builder = ReplyKeyboardBuilder()
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
    builder.button(text="Главное меню 🔙")
    return builder.as_markup(resize_keyboard=True)

def back_arrow_button():
    """Кнопка назад"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="Назад⏪")
    return builder.as_markup(resize_keyboard=True)
