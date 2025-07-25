from tronpy import Tron
from app.schemas.tron import TronAddressResponse

async def get_tron_address_info(address: str) -> TronAddressResponse:
    client = Tron()
    try:
        acc_info = client.get_account(address)
        balance = client.get_account_balance(address)
        resources = client.get_account_resource(address)
        return TronAddressResponse(
            address=address,
            balance=float(balance),
            bandwidth=resources.get('free_net_used', 0),
            energy=resources.get('EnergyUsed', 0)
        )
    except Exception:
        return None 