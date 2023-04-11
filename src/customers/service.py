from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import models, schemas


async def get_customer(db: AsyncSession, customerId: int):
    result = await (db.execute(select(models.Customer).filter(
        models.Customer.customerId == customerId)))
    customer = result.first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer[0]


async def create_customer(db: AsyncSession, customer: schemas.Customer):
    db_customer = models.Customer(
        customerId=customer.customerId,
        name=customer.name,
        address=customer.address)
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer


async def update_customer(
        db: AsyncSession, customerId: int, customer: schemas.Customer
):
    original = await get_customer(db, customerId)
    original.name = customer.name
    original.address = customer.address
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_customer(db: AsyncSession, customerId: int):
    original = await get_customer(db, customerId)
    await db.delete(original)
    await db.commit()
