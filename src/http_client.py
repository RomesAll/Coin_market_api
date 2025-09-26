from httpx import AsyncClient
from config import settings
import asyncio

class HTTPClient:
    def __init__(self, base_url: str, key: str):
        self._async_client = AsyncClient(base_url=base_url, 
                                   headers={'X-CMC_PRO_API_KEY': key})

class CoinMarketCapHTTPClient(HTTPClient):
    async def get_list_coin(self):
        async with self._async_client as client:
            response = await client.get("/v1/cryptocurrency/listings/latest")
            return response.json()['data']
    
    async def get_currents_coin(self, id: int):
        async with self._async_client as client:
            response = await client.get("/v2/cryptocurrency/quotes/latest", params={"id": id})
            return response.json()['data'][str(id)]