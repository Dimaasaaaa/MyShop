from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.base import engine
from database.models import (Users, Products, Carts, Orders, Categories, FinallyCarts)
from sqlalchemy import update, select, func, join, DECIMAL


def get_session():
    return Session(engine)


def db_register_user(full_name: str, chat_id: int):
    """Регистрация юзера в базе"""

    try:
        with get_session() as session:
            query = Users(name=full_name, telegram=chat_id)
            session.add(query)
            session.commit()
        return False
    except IntegrityError:
        return True


def db_update_user(chat_id: int, phone: str):
    """обновляем данные пользователя, получаем номер телефона"""

    with get_session() as session:
        query = update(Users).where(Users.telegram == chat_id).values(phone=phone)
        session.execute(query)
        session.commit()


def db_create_user_cart(chat_id):
    """создание корзины пользователя после регистрации"""
    try:
        with get_session() as session:
            user = session.scalar(select(Users).where(Users.telegram == chat_id))
            if user is None:
                return False
            query = Carts(user_id=user.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False


def db_get_all_category():
    """получение всех категорий"""
    with get_session() as session:
        query = select(Categories)
        return session.scalars(query).all()


def db_get_finally_price(chat_id):
    """Получение итоговой цены"""
    with get_session() as session:
        query = select(func.sum(FinallyCarts.final_price)).select_from(
            join(Carts, FinallyCarts, Carts.id == FinallyCarts.cart_id)
            .join(Users, Users.id == Carts.user_id)
            .where(Users.telegram == chat_id)
        )
        return session.execute(query).scalar()


def db_get_last_orders(chat_id, limit = 10):
    """Получение истории заказов"""
    with get_session() as session:
        query = (
            select(Orders).
            join(Carts, Orders.cart_id == Carts.id).
            join(Users, Users.id == Carts.user_id).
            where(Users.telegram == chat_id).
            order_by(Orders.id.desc()).
            limit(limit)
        )
        return session.scalars(query).all()

def db_get_products(category_id):
    """Получение продуктов по id категории"""
    with get_session() as session:
        query = select(Products).where(Products.category_id == category_id)
        return session.execute(query).all()

def db_get_products_by_id(product_id):
    """Получение продукта по его id"""
    with get_session() as session:
        return session.scalar(select(Products).where(Products.id == product_id))


def db_get_user_cart(chat_id):
    """Получение корзины пользователя по его ID"""
    with get_session() as session:
        return session.scalar(select(Carts).join(Users, Users.id == Carts.user_id)
                              .where(Users.telegram == chat_id))

def db_add_or_update_item(
        cart_id: int,
        product_id: int,
        product_name: str,
        product_price: DECIMAL,
        increment: int = 0):
    """Добавление или изменение товара"""
    try:
        with get_session() as session:
            item = (session.query(FinallyCarts)
                    .filter_by(cart_id=cart_id, product_id=product_id)
                    .first())

            if item:
                if increment != 0:
                    item.quantity = max(1, item.quantity + increment)
                else:
                    item.quantity = max(1, increment)
            else:
                item = FinallyCarts(
                    cart_id=cart_id,
                    product_id=product_id,
                    product_name=product_name,
                    quantity=max(1, increment),
                    final_price=0
                )
                session.add(item)

            item.final_price = item.quantity * product_price

            total_price, total_products = session.query(
                func.coalesce(func.sum(FinallyCarts.final_price), 0),
                func.coalesce(func.sum(FinallyCarts.quantity), 0)
            ).filter(
                FinallyCarts.cart_id == cart_id,
            ).one()

            session.query(Carts).filter(
                Carts.id == cart_id,
            ).update({
                Carts.total_price: total_price,
                Carts.total_products: total_products,
            })
            session.commit()

            return {
                "status": "ok",
                "total_price": float(total_price),
                "product_quantity": item.quantity,
            }
    except Exception as e:
        print(e)
        return {
            "status": "error",
        }
