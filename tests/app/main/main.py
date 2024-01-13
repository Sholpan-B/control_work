import fastapi
import pydantic
from fastapi.staticfiles import StaticFiles

from tortoise.contrib.fastapi import register_tortoise

from tests.app.main.routers import test
from config import TORTOISE_ORM
from exceptions import handlers as exc_handlers, http as http_exc


def setup():
    app = fastapi.FastAPI()
    app.include_router(test.router)

    register_tortoise(
        app=app, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True,
    )

    app.exception_handler(pydantic.ValidationError)(exc_handlers.query_params_exc_handler)
    app.exception_handler(http_exc.BaseHTTPException)(exc_handlers.request_exc_handler)
    app.exception_handler(500)(exc_handlers.internal_exc_handler)

    app.mount('/media', StaticFiles(directory='media'), name='media')

    return app


app = setup()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=1028, reload=True)