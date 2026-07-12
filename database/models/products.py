from sqlalchemy import String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .categories import Categories
from ..base import Base


class Products(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(String(365))
    image: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(DECIMAL(10, 2))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    product_category: Mapped[Categories] = relationship(back_populates='products')