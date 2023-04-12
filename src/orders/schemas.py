from datetime import date
from pydantic import BaseModel


class OrderDetail(BaseModel):
    orderId: int | None
    rowNumber: int
    productId: int
    quantity: int
    pricePerUnit: int

    class Config:
        orm_mode = True


class OrderHeader(BaseModel):
    orderId: int
    customerId: int
    orderDate: date
    details: list[OrderDetail] = []

    class Config:
        orm_mode = True
