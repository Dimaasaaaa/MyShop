from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, FSInputFile
from database.utils import db_get_products_by_id, db_get_user_cart


router = Router()

@router.callback_query(F.data.startswith("product_view"))
async def show_product_details(callback: CallbackQuery, bot: Bot):
    """Показ деталей товара"""

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id, message_id)

    product_id = callback.data.split('_')[-1]
    product = db_get_products_by_id(product_id)

    user_cart = db_get_user_cart(chat_id)
    if user_cart:
        db_add_or_update_item()
        caption = text_for_caption()
        product_image = FSInputFile(path=product.image)
    await bot.send_photo(chat_id=chat_id,
                         photo=product_image,
                         caption=caption,
                         parse_mode="html",
                         reply_markup=quantity_cart_controls())

