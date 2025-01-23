import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine


# Load environment variables from the .env file
load_dotenv()

def main():
    # Fetching environment variables from .env file
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db = os.getenv('POSTGRES_DB')
    table_name = os.getenv('TABLE_NAME')
    url = os.getenv('URL')

    parquet_name = 'parquet_name.parquet'
    os.system(f"wget {url} -O {parquet_name}")

    # Create a SQLAlchemy engine for the PostgreSQL connection
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_parquet(parquet_name, engine='pyarrow') 
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    chunk_size = 50000

    # Loop through the DataFrame in chunks and insert them into the PostgreSQL table
    for start in range(0, len(df), chunk_size):
        chunk = df.iloc[start:start + chunk_size]
        # Append the chunk to the PostgreSQL table
        chunk.to_sql(table_name, engine, if_exists='append', index=False, method='multi')
        print(f"Inserted chunk with {len(chunk)} rows")


if __name__ == '__main__':
    main()
