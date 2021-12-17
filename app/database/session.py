from sqlalchemy import create_engine, engine #hace la conexion a la bdd
from sqlalchemy.orm import sessionmaker #orm (obj relac bdd (obj en la bdd))
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from app.core.config import settings

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_pring=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()