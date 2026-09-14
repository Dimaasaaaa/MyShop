from sqlalchemy import String, DECIMAL, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.base import Base


class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    product_name: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int]
    final_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __str__(self):
        return f'{self.product_name} {str(self.quantity)} {str(self.final_price)} ₽'