from sqlalchemy import BigInteger, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.base import Base
from .users import Users


class Carts(Base):
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    total_price: Mapped[int] = mapped_column(DECIMAL(10, 2), default=0)
    total_products: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)

    user_cart: Mapped['Users'] = relationship(back_populates='carts')
    finally_id: Mapped[list['FinallyCarts']] = relationship('FinallyCarts', back_populates='user_cart')


class FinallyCarts(Base):
    __tablename__ = 'final_carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product_name: Mapped[str] = mapped_column(String(40))
    final_price: Mapped[int] = mapped_column(default=0)
    quantity: Mapped[int]

    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    user_cart: Mapped['Carts'] = relationship(back_populates='finally_id')