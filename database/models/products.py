from sqlalchemy import String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .categories import Categories

class Products(Base):
    __table_name__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(String(365))
    image: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(DECIMAL(10, 2))

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    product_category: Mapped[Categories] = relationship(bask_populates='products')