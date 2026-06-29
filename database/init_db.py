from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from database.base import Base, engine
from database.models import Users, Carts, FinallyCarts, Categories, Products, Orders

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def init_db():
    """фунция для ззаполнения бд тестовыми данными"""
    print("Создаём таблицы...")

    Base.metadata.create_all(bind=engine)

    print("Таблицы готовы!")

    with SessionLocal() as session:

        categories = ["Торты", "Печенье", "Пирожные"]
        category_map = {}

        for name in categories:
            category = session.scalar(
                select(Categories).filter_by(category_name=name)
            )

            if not category:
                category = Categories(category_name=name)
                session.add(category)
                session.flush()

            category_map[name] = category.id

        products = [
            ("Торты", "Медовик", 45, "мёд, мука, сахар, яйца, масло", "media/cakes/hone_cake.jpg"),
            ("Торты", "Наполеон", 55, "молоко, мука, сахар, яйца, масло", "media/cakes/cake_napoleon.jpg"),
            ("Печенье", "Шоколадное печенье", 20, "шоколад, мука, сахар, яйца, масло",
             "media/cookies/choco_cookie.jpg"),
            ("Печенье", "Кокосовое печенье", 25, "кокос, мука, сахар, яйца, масло", "media/cookies/kokos_cookie.jpg"),
            ("Пирожные", "Эклер", 30, "мука, яйца, масло, шоколад", "media/cakes/eclair.jpg"),
            ("Пирожные", "Картошка", 35, "печенье, сгущёнка, какао, масло", "media/cakes/kar-toshka.jpg"),
        ]

        for category_name, name, price, desc, image in products:

            exists = session.scalar(
                select(Products).filter_by(product_name=name)
            )

            if not exists:
                session.add(
                    Products(
                        category_id=category_map[category_name],
                        product_name=name,
                        price=price,
                        description=desc,
                        image=image
                    )
                )

        session.commit()
        print("Данные добавлены!")


if __name__ == "__main__":
    init_db()