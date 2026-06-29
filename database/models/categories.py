from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Categories(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(25), unique=True)

    products = relationship('Products', back_populates='product_category')
