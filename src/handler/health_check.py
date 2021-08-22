from fastapi import APIRouter
from src import __version__

hc_router = APIRouter()


@hc_router.get('/hc')
def health_check():
    return {
        'version': __version__,
        'status': 'alive and kicking'
    }
