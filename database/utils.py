from idlelib import query

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.base import engine
from database.models import (Users,Products,Carts,Orders,Categories,FinallyCarts)
from sqlalchemy import update


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
    """"создание корзины пользователя после регистрации"""
    try:
        with get_session() as session:
            subquery = session.scalar(select(Users).where(Users.telegram == chat_id))
            query = Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False
def db_get_all_category():
    '''получение всех категорий'''
    with get_session() as session:
        query = select(Categories)
        return session.scalars(query).all

def db_get_finally_price(chat_id)
    """Попытка установить цену"""
    with get_session() as session:
        query = select(func.sum(FinallyCarts.final_price)).select_from(
            join(Carts, FinallyCarts, Carts.id == FinallyCarts.cart_id)
            .join(Users, Users.id == Carts.user_id)
            .where(Users.telegram == chat_id)
        )
        return session.execute(query).scalar()