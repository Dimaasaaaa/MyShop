from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from database.utils import db_get_cart_items
from keyboards.inline import cart_actions_kb

router = Router()

@router.message(F.text=='Оформить заказ 🚚')
async def handle_cart(message: Message):
    '''демонстрация твоаров в корзине reply-клавиатурой'''
    await show_cart(chat_id=message.chat.id, send_fn=message.answer)

@router.callback_query(F.data == 'корзина заказа')
async def open_cart(callback: CallbackQuery):
    '''демонстрация твоаров в корзине inline-клавиатурой'''
    await show_cart(chat_id=callback.chat.id, send_fn=callback.answer)
    await callback.answer()

async def show_cart(chat_id, send_fn):
    '''демонстрация корзины'''
    cart_items = db_get_cart_items(chat_id)
    if not cart_items:
        await send_fn('В корзине пусто')
        return
    text = 'В корзине 🛒'
    total = 0
    for item in cart_items:
        total = float(item['final_price']) + total
        text += f'{item['product_name']} - {item['quantity']} шт - {item['final_price']} руб. \n'
    text += f'цена: {total:.2F} руб \n'

    await send_fn(text, reply_markup=cart_actions_kb())