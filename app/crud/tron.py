from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tron import TronAddressRequestDB
from app.schemas.tron import TronAddressResponse, TronAddressHistoryResponse, TronAddressHistoryItem

async def create_tron_request(db: AsyncSession, address: str, info: TronAddressResponse):
    db_obj = TronAddressRequestDB(
        address=address,
        balance=info.balance,
        bandwidth=info.bandwidth,
        energy=info.energy
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_tron_requests(db: AsyncSession, skip: int = 0, limit: int = 10) -> TronAddressHistoryResponse:
    q = await db.execute(select(TronAddressRequestDB).order_by(TronAddressRequestDB.created_at.desc()).offset(skip).limit(limit))
    items = q.scalars().all()
    total = await db.scalar(select(func.count()).select_from(TronAddressRequestDB))
    return TronAddressHistoryResponse(
        total=total,
        items=[TronAddressHistoryItem(
            id=i.id,
            address=i.address,
            balance=i.balance,
            bandwidth=i.bandwidth,
            energy=i.energy,
            created_at=i.created_at.isoformat()
        ) for i in items]
    ) 