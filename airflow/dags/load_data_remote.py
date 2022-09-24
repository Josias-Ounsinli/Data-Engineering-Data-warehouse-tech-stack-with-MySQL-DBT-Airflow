from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import date, datetime

import sys
import os

sys.path.append(os.path.abspath(os.path.join("../general_scripts_notebooks")))
sys.path.append(os.path.abspath(os.path.join("./include")))
sys.path.append(os.path.abspath(os.path.join("../data")))


# from data_extract import DataExtractor
# extractor = DataExtractor()

import pandas as pd
from sqlalchemy import text

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:IQVEgjpdlDmTEZkDemIt@containers-us-west-72.railway.app:7362/railway')

CARS_SCHEMA = "./dags/include/CARS_schema.sql"
TRAJECTORIES_SCHEMA = "./dags/include/TRAJECTORIES_schema.sql"

# def create_table():
#     try:
#         with engine.connect() as conn:
#             for name in [CARS_SCHEMA, TRAJECTORIES_SCHEMA]:
#                 with open(f'{name}') as file:
#                     query = text(file.read())
#                     conn.execute(query)
#         print("Successfull")
#     except Exception as e:
#         print(e)


def insert_to_car_table_remote():
    try:
        df_car = pd.read_csv('./dags/include/cars_table.csv')
        #df_traj = pd.read_csv('./dags/include/trajectories_table.csv')
        with engine.connect() as conn:
            df_car.to_sql(name='cars', con=conn, if_exists='replace', index=False)
            #df_traj.to_sql(name='trajectories', con=conn, if_exists='replace', index=False)
        print("Successfull")
    except Exception as e:
        print(f"Failed  ---- {e}")  


def insert_to_traj_table_remote():
    try:
        # df_car = pd.read_csv('./dags/include/cars_table.csv')
        df_traj = pd.read_csv('./dags/include/trajectories_table.csv')
        with engine.connect() as conn:
            #df_car.to_sql(name='cars', con=conn, if_exists='replace', index=False)
            df_traj.to_sql(name='trajectories', con=conn, if_exists='replace', index=False)
        print("Successfull")
    except Exception as e:
        print(f"Failed  ---- {e}")

with DAG(
        dag_id = 'loading_data_remote',
        description='Load data in remote postgres database',
        schedule_interval='@once',
        start_date=datetime(2022,1,1),
        catchup=False
    ) as dag:

        # table_creation = PythonOperator(
        #     task_id='create_tables',
        #     python_callable=create_table
        # )

        load_data_remote = PythonOperator(
            task_id='load_car_tables_remote',
            python_callable=insert_to_car_table_remote
        )

        load_data2_remote = PythonOperator(
            task_id='load_traj_tables_remote',
            python_callable=insert_to_traj_table_remote
        )

        load_data_remote >> load_data2_remote