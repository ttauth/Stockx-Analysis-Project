import pandas as pd
import glob
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}")

def chunk_df(df, chunk_size):
    for start in range(0, df.shape[0], chunk_size):
        yield df.iloc[start:start + chunk_size]

file = 'StockX-Data-Contest-2019-3.csv'
df = pd.read_csv(file, low_memory=False)  
table_name = 'StockX_Data'  

with engine.connect() as connection:
    connection.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))

for chunk in chunk_df(df, 200): 
    chunk.to_sql(table_name, engine, if_exists='append', index=False)
    print(f'Inserted chunk into {table_name}')

print('The stockx data table has been imported into the database.')
