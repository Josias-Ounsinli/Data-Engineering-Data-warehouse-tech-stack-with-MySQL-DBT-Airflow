from airflow import DAG

from datetime import datetime

import pandas as pd
from sqlalchemy import text

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:root@host.docker.internal/trafficdatabase')

CAR_SCHEMA = "CARS_schema.sql"
TRAJECTORIES_SCHEMA = "TRACJECTORIES_schema.sql"

def create_table():
    try:
        with engine.connect() as conn:
            for name in [CAR_SCHEMA, TRAJECTORIES_SCHEMA]:
                with open(f'{name}') as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfull")
    except Exception as e:
        print(e)

