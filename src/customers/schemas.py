from pydantic import BaseModel


class Customer(BaseModel):
    customerId: int
    name: str
    address: str

    class Config:
        orm_mode = True
