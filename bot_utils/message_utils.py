def text_for_caption(name, description, base_price):
    """Описание товара"""
    text = (
        f"<b>{name}</b>n"
        f"<b>Описание: {description}</b>\n"
        f"<b>Цена: {float(base_price)}</b>\n"
    )
    return text