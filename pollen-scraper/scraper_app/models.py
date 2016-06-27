from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, Float, String

import settings

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_forecast_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Forecasts(DeclarativeBase):
    __tablename__ = 'forecasts'

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    pollen_value = Column('pollen_value', Float, nullable=True)
    severity = Column('severity', String, nullable=True)
    top_allergens = Column('top_allergens', String, nullable=True)
