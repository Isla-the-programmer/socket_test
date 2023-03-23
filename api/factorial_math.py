from fastapi import APIRouter
from fastapi.websockets import WebSocket
import math

router = APIRouter()


@router.websocket("/factorial-math")
async def websocket(socket: WebSocket):
    await socket.accept()
    data = await socket.receive_text()
    try:
        number = int(data)
        factorial_n = math.factorial(number)
        await socket.send_text(str(factorial_n))
    except ValueError:
        await socket.send_text("no_factorial")
    await socket.close()
