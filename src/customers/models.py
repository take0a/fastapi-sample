from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Customer(Base):
    __tablename__ = "customer"

    customerId: Mapped[int] = mapped_column(
        name="customer_id", primary_key=True)
    name: Mapped[str]
    address: Mapped[str]

    def __repr__(self) -> str:
        return f"Customer(customerId={self.customerId!r}, " \
            f"name={self.name!r}, address={self.address!r})"
