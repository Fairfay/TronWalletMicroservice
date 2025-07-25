import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.tron import TronAddressRequestDB
from app.schemas.tron import TronAddressResponse
from app.crud.tron import create_tron_request
from app.core.db import Base
import asyncio

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.mark.asyncio
async def test_create_tron_request():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        info = TronAddressResponse(address="TXYZ...abc", balance=1.23, bandwidth=100, energy=200)
        obj = await create_tron_request(session, "TXYZ...abc", info)
        assert obj.id is not None
        assert obj.address == "TXYZ...abc"
        assert obj.balance == 1.23
        assert obj.bandwidth == 100
        assert obj.energy == 200 