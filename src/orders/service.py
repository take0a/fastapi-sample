from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import models, schemas


async def get_order(db: AsyncSession, orderId: int) -> models.OrderHeader:
    result = await (db.execute(select(models.OrderHeader).filter(
        models.OrderHeader.orderId == orderId)))
    order = result.first()
    if order is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return order[0]


async def create_order(db: AsyncSession, order: schemas.OrderHeader):
    db_details = []
    for detail in order.details:
        db_details.append(models.OrderDetail(
            orderId=order.orderId,
            rowNumber=detail.rowNumber,
            productId=detail.productId,
            quantity=detail.quantity,
            pricePerUnit=detail.pricePerUnit,
        ))
    db_order = models.OrderHeader(
        orderId=order.orderId,
        customerId=order.customerId,
        orderDate=order.orderDate,
        details=db_details)
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order


async def update_order(
        db: AsyncSession, orderId: int, order: schemas.OrderHeader
):
    original = await get_order(db, orderId)
    original.customerId = order.customerId
    original.orderDate = order.orderDate
    original.details.clear()
    for detail in order.details:
        original.details.append(models.OrderDetail(
            orderId=orderId,
            rowNumber=detail.rowNumber,
            productId=detail.productId,
            quantity=detail.quantity,
            pricePerUnit=detail.pricePerUnit,
        ))
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_order(db: AsyncSession, orderId: int):
    original = await get_order(db, orderId)
    await db.delete(original)
    await db.commit()
