from fastapi import APIRouter, Depends
from http_client import CoinMarketCapHTTPClient
from typing import Annotated
from config import settings

router = APIRouter()

cmc_depends = Annotated[CoinMarketCapHTTPClient, Depends(CoinMarketCapHTTPClient)]

@router.get('/coins')
async def get_all_coins(params: cmc_depends):
    return await params.get_list_coin()

@router.get('/coins/{id_coin}')
async def get_current_coins(id_coin, params: cmc_depends):
    return await params.get_currents_coin(id_coin)
