import uvicorn

from fastapi import FastAPI, HTTPException

from src import __version__
from src.handler.user import user_router
from src.handler.product import product
from src.settings import *

app = FastAPI(
    title="Teste com fast Api",
    description="Verificando rotas da api",
    version=__version__
)

app.include_router(user_router, prefix=BASE_PATH)
app.include_router(product, prefix=BASE_PATH)


@app.exception_handler(HTTPException)
async def http_error(request):
    return {"error": "HTTPException"}

if __name__ == '__main__':
    uvicorn.run(
        app,
        debug=False,
        timeout_keep_alive=50
    )