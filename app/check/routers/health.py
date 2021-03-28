from datetime import datetime

from fastapi import APIRouter, Request


router = APIRouter()


@router.get('/')
@router.get('/hello')
async def say_hello(request: Request):
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now().strftime(fmt)
    client_host = request.client.host
    return {'message': 'Hello world', 'now': now, 'ip': client_host}
