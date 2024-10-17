from ..relational.ModelBase import Base
from .get_vector_engine import get_vector_engine, get_vectordb_config
from sqlalchemy import text

async def create_db_and_tables():
    vector_config = get_vectordb_config()
    vector_engine = get_vector_engine()

    if vector_config.vector_engine_provider == "pgvector":
        async with vector_engine.engine.begin() as connection:
            if len(Base.metadata.tables.keys()) > 0:
                await connection.run_sync(Base.metadata.create_all)
            await connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
         
            