from fastapi import FastAPI
from routers.coin_market_cap_api import router as router_coin_api
import uvicorn

app = FastAPI()
app.include_router(router_coin_api)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8000)