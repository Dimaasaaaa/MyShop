from sqlalchemy import BigInteger, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(35))
    telegram: Mapped[int] = mapped_column(BigInteger, unique=True)
    phone: Mapped[str] = mapped_column(String(15),nullable=True)