from pydantic import BaseModel


class Product(BaseModel):
    productId: int
    name: str
    pricePerUnit: int

    class Config:
        orm_mode = True
