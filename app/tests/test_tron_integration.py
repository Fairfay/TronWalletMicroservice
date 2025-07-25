import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_tron_address_flow():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # POST запрос
        resp = await ac.post("/tron/address", json={"address": "TXYZ...abc"})
        assert resp.status_code in (200, 404)  # 404 если адрес тестовый
        if resp.status_code == 200:
            data = resp.json()
            assert "balance" in data
            assert "bandwidth" in data
            assert "energy" in data
        # GET история
        resp = await ac.get("/tron/history?skip=0&limit=5")
        assert resp.status_code == 200
        data = resp.json()
        assert "items" in data
        assert "total" in data 