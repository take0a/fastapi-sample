from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Product(Base):
    __tablename__ = "product"

    productId: Mapped[int] = mapped_column(
        name="product_id", primary_key=True)
    name: Mapped[str]
    pricePerUnit: Mapped[int] = mapped_column(name="price_per_unit")

    def __repr__(self) -> str:
        return f"Product(productId={self.productId!r}, " \
            f"name={self.name!r}, address={self.pricePerUnit!r})"
