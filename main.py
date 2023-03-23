from fastapi import FastAPI
from api import factorial_math, factorial_recursive, factorial_continuous
import uvicorn

app = FastAPI()
app.include_router(factorial_math.router)
app.include_router(factorial_recursive.router)
app.include_router(factorial_continuous.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
