from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.base import engine
from database.models import (Users,Products,Carts,Orders,Categories,FinallyCarts)


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
    pass