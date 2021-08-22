import uvicorn

from fastapi import FastAPI, HTTPException

from src import __version__

from src.handler import *
from src.settings import *

app = FastAPI(
    title="Teste com fast Api",
    description="Verificando rotas da api",
    version=__version__
)

app.include_router(hc_router, prefix=BASE_PATH)
app.include_router(user_router, prefix=BASE_PATH)
app.include_router(product_router, prefix=BASE_PATH)
app.include_router(category_router, prefix=BASE_PATH)
app.include_router(item_cart_router, prefix=BASE_PATH)


@app.exception_handler(HTTPException)
async def http_error(request):
    return {"error": "HTTPException"}

if __name__ == '__main__':
    uvicorn.run(
        app,
        debug=False,
        timeout_keep_alive=50
    )