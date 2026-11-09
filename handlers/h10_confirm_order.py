from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from database.utils import db_get_user_phone, db_save_order_history, db_clear_final_cart
router = Router()

@router.callback_query(F.data=="confirm_order")
async def confirm_order(callback: CallbackQuery, bot: Bot):
    """подтверждение заказов"""
    user = callback.from_user
    phone = db_get_user_phone(user.id)
    mention = f"<a href='tg://user?=id{user.id}'>{user.full_name}</a>"
    user_text = f"Новый заказ от {mention}\nс номером телефона {phone}"
    context = counting_products_from_cart(user.id, user_text)

    if not context:
        await bot.send_message.edit_text("Корзина пуста. Выберите товар")
        await callback.answer()
        return
    if not ADMIN_ID:
        await bot.send_message.edit_text("Менеджер неуказан")
        await callback.answer()
        return

    count,text, total_price, cart_id = context
    await bot.send_message(cart_id=ADMIN_ID,text=context,parse_mode="HTML")

    db_save_order_history(chat_id)

    db_clear_final_cart(callback.from_user.id)

    await callback.message.edit_text("Ваш заказ оформлен✅. Для связи с админом нажмите кнопку в настройках")
    await callback.answer("Заказ оформлен")
