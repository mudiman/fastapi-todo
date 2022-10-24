from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ASYNC_DB_URL = "postgresql://admin:donotusethispassword@localhost:15813/todo"


engine = create_async_engine(ASYNC_DB_URL, echo=True, future=True)

async_session = sessionmaker(
    autoflush=True, bind=engine, class_=AsyncSession, future=True
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session