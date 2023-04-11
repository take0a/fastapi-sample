from sqlalchemy import Column, Integer, String

from src.database import Base


class Customer(Base):
    __tablename__ = "customer"

    customerId = Column(Integer, name="customer_id",
                        primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
