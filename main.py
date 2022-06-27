import uvicorn
import logging

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.app.user import router as user_router
from app.app.light import router as lights_router
from app.database import db
from app.utils.utils import load_config
from app.utils.serial_utils import serial_communicator

app = FastAPI()

config = load_config("config/config.yaml")
logger = logging.getLogger('uvicorn.info')


@app.on_event("startup")
async def setup_app() -> None:
    db_config = config["db"]
    db_uri = f"{db_config['driver']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"

    logger.info(f"Connected to database: {db_uri}")

    await db.set_bind(db_uri)

    # serial_communicator.setup()


@app.on_event("shutdown")
async def setup_app() -> None:
    await db.pop_bind().close()

    logger.info(f"Disconnected from database")

    # serial_communicator.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(user_router)
app.include_router(lights_router)


if __name__ == "__main__":
    config_server = config["server"]

    uvicorn.run(
        "main:app",
        host=config_server["host"],
        port=config_server["port"],
        reload=True,
    )
