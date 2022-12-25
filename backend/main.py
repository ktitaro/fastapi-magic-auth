from fastapi import FastAPI, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from miniapps.auth.controllers import router as auth_router
from miniapps.users.controllers import router as users_router
from settings.database import DATABASE_URL

def setup_routes(app: FastAPI):
    core_router = APIRouter()
    core_router.include_router(auth_router, prefix='/auth', tags=['auth'])
    core_router.include_router(users_router, prefix='/users', tags=['users'])
    app.include_router(core_router, prefix='/api')

def setup_database(app: FastAPI):
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        generate_schemas=True,
        add_exception_handlers=True,
        modules={
            'models': [
                'miniapps.auth.models',
                'miniapps.users.models',
            ],
        },
    )

app = FastAPI()
setup_routes(app)
setup_database(app)
