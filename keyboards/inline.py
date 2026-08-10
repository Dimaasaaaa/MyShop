from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import db_get_all_category, db_get_finally_price

def create_categories_menu(chat_id):
    """Предоставление меню с категориями продуктов"""
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(text=f"Корзина заказа ({total_price if total_price else 0}₽)",
                   callback_data="корзина заказа"
                   )
    [builder.button(text=categories.category_name, callback_data = f"category_{category.id}")for category in categories]

    builder.adjust(2,1)
    return builder.as_markup()