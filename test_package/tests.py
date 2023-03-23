from fastapi.testclient import TestClient
from main import app
import pytest

testdata = [
    ('-1', 'no_factorial'),
    ('0', '1'),
    ('1', '1'),
    ('5', '120'),
    ('10', '3628800')
]


@pytest.mark.parametrize("number, result", testdata)
def test_math_factorial(number: str, result: str):
    client = TestClient(app)
    with client.websocket_connect("/factorial-math") as websocket:
        websocket.send_text(number)
        data = websocket.receive_text()
        assert data == result


@pytest.mark.parametrize("number , result", testdata)
def test_recursive_factorial(number: str, result: str):
    client = TestClient(app)
    with client.websocket_connect("/factorial-recursive") as websocket:
        websocket.send_text(number)
        data = websocket.receive_text()
        assert data == result
