import logging

from app.core.config import DATABASE_URL
from databases import Database
from fastapi import FastAPI

logger = logging.getLogger(__name__)

# PostgreSQLへの接続を確立
async def connect_to_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=5)

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DATABASE CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE CONNECTION ERROR ---")


# データベースから切断する
async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DATABASE DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE DISCONNECT ERROR ---")