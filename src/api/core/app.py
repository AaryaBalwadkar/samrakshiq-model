from fastapi import FastAPI
from ..config.env_loader import load_env
from ...utils.logging.setup import setup_logger
from ..routes.health.check import router as health_router

env = load_env()
logger = setup_logger(env["LOG_LEVEL"])

app = FastAPI(title="SamrakshIQ", json_serializer="orjson")

app.include_router(health_router)

@app.on_event("startup")
async def startup():
    logger.info("SamrakshIQ API started")