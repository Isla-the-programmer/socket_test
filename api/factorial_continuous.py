from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocket
import math


router = APIRouter()


@router.get("/")
async def get():
    with open("templates/index.js") as template:
        index_template = template.read()
        return HTMLResponse(index_template)


@router.websocket("/continuous")
async def websocket(socket: WebSocket):
    await socket.accept()
    while True:
        data = await socket.receive_text()
        try:
            number = int(data)
            factorial_n = math.factorial(number)
            await socket.send_text(f'Factorial of given number({data}): {str(factorial_n)}')
        except ValueError:
            await socket.send_text("no_factorial")
