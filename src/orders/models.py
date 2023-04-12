from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class OrderHeader(Base):
    __tablename__ = "order_header"

    orderId: Mapped[int] = mapped_column(
        name="order_id", primary_key=True)
    customerId: Mapped[int] = mapped_column(name="customer_id")
    orderDate: Mapped[date] = mapped_column(name="order_date")
    details: Mapped[list["OrderDetail"]] = relationship(
        cascade="all, delete", lazy="joined")

    def __repr__(self) -> str:
        return f"OrderHeader(orderId={self.orderId!r}, " \
            f"customerId={self.customerId!r}, orderDate={self.orderDate!r})"


class OrderDetail(Base):
    __tablename__ = "order_detail"

    orderId: Mapped[int] = mapped_column(
        ForeignKey("order_header.order_id"),
        name="order_id", primary_key=True)
    rowNumber: Mapped[int] = mapped_column(
        name="row_number", primary_key=True)
    productId: Mapped[int] = mapped_column(name="product_id")
    quantity: Mapped[int]
    pricePerUnit: Mapped[int] = mapped_column(name="price_per_unit")

    def __repr__(self) -> str:
        return f"OrderDetail(orderId={self.orderId!r}, " \
            f"rowNumber={self.rowNumber!r}, productId={self.productId!r})" \
            f"quantity={self.quantity!r}, pricePerUnit={self.pricePerUnit!r})"
