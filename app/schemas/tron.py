from pydantic import BaseModel, Field
from typing import List, Optional

class TronAddressRequest(BaseModel):
    address: str = Field(..., example="TXYZ...abc")

class TronAddressResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int

class TronAddressHistoryItem(BaseModel):
    id: int
    address: str
    balance: float
    bandwidth: int
    energy: int
    created_at: str

class TronAddressHistoryResponse(BaseModel):
    total: int
    items: List[TronAddressHistoryItem] 