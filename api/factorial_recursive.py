from fastapi import APIRouter
from fastapi.websockets import WebSocket

router = APIRouter()


def factorial_recursive(number: int):
    if number == -1:
        raise ValueError
    if number == 1 or number == 0:
        return 1
    return number * factorial_recursive(number-1)


@router.websocket("/factorial-recursive")
async def websocket(socket: WebSocket):
    await socket.accept()
    data = await socket.receive_text()
    try:
        number = int(data)
        factorial_n = factorial_recursive(number)
        await socket.send_text(str(factorial_n))
    except ValueError:
        await socket.send_text("no_factorial")
    await socket.close()
