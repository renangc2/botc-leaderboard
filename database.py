from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 优先读取系统环境变量 `DATABASE_URL` (用于云端 PostgreSQL)
# 如果没找到，则默认使用本地 SQLite 数据库进行开发和测试
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./botc.db")

# 如果使用的是 SQLite，需要特别声明 check_same_thread=False
# 如果是云端的 PostgreSQL (通常以 postgresql:// 或 postgres:// 开头)，则不需要
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # 兼容有些平台(如 Render, Heroku)提供的 URL 是 postgres://，SQLAlchemy 1.4+ 要求必须是 postgresql://
    if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
