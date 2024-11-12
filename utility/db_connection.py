import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

# Replace with below code for sqlserver
# username = os.getenv("DB_USERNAME")
# password = os.getenv("DB_PASSWORD")
# server = os.getenv("DB_SERVER")
# database = os.getenv("DB_NAME")
# DATABASE_URL = f"mssql+aioodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes

engine = create_async_engine(DATABASE_URL, pool_size=20)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,class=AsyncSession)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
