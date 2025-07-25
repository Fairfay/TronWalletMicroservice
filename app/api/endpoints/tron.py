from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tron import TronAddressRequest, TronAddressResponse, TronAddressHistoryResponse
from app.services.tron import get_tron_address_info
from app.crud.tron import create_tron_request, get_tron_requests
from app.models.database import get_session

router = APIRouter()

@router.post("/address", response_model=TronAddressResponse)
async def get_address_info(
    data: TronAddressRequest,
    db: AsyncSession = Depends(get_session)
):
    info = await get_tron_address_info(data.address)
    if not info:
        raise HTTPException(status_code=404, detail="Address not found or invalid")
    await create_tron_request(db, data.address, info)
    return info

@router.get("/history", response_model=TronAddressHistoryResponse)
async def get_history(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_session)
):
    return await get_tron_requests(db, skip=skip, limit=limit) 