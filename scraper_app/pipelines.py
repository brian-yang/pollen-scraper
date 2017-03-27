from sqlalchemy.orm import sessionmaker
from models import Forecasts, db_connect, create_forecast_table

import logging

class PollenScraperPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_forecast_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        forecast = Forecasts(**item)
        try:
            session.add(forecast)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
