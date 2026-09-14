from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.utils import db_get_all_category, db_get_finally_price, db_get_products


def create_categories_menu(chat_id):
    """Предоставление меню с категориями продуктов"""
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(text=f"корзина заказа ({total_price if total_price else 0}руб.)",
                   callback_data="корзина заказа"
                   )
    [builder.button(text=category.category_name, callback_data = f"category_{category.id}") for category in categories]

    builder.adjust(2, 1)
    return builder.as_markup()

def show_product_by_category(category_id):
    """Показ товаров по категориям"""
    products = db_get_products(category_id)
    builder = InlineKeyboardBuilder()
    [builder.button(text=product.product_name, callback_data=f"product_view_{product.id}") for product in products]
    builder.adjust(3)
    builder.row(InlineKeyboardButton(text="➤ Назад", callback_data="from_detail_to_category"))
    return builder.as_markup()