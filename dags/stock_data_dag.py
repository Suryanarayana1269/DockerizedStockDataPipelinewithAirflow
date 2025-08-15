from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import psycopg2
import logging

API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
SYMBOL = os.environ.get('STOCK_SYMBOL')
DB_CONN = "dbname='stocks' user='postgres' password='postgres' host='postgres' port='5432'"

def fetch_and_store_stock_data():
    try:
        # Fetch
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=60min&apikey={API_KEY}"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        time_series = data.get("Time Series (60min)", {})
        if not time_series:
            logging.warning("No time series data found")
            return

        # Save to DB
        conn = psycopg2.connect(DB_CONN)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock_data (
                timestamp TIMESTAMP PRIMARY KEY,
                open FLOAT,
                high FLOAT,
                low FLOAT,
                close FLOAT,
                volume BIGINT
            )
        """)
        # Pick latest datapoint
        latest_ts = sorted(time_series.keys())[-1]
        dp = time_series[latest_ts]
        cursor.execute("""
            INSERT INTO stock_data (timestamp, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (timestamp) DO NOTHING
        """, (
            latest_ts,
            float(dp["1. open"]),
            float(dp["2. high"]),
            float(dp["3. low"]),
            float(dp["4. close"]),
            int(dp["5. volume"])
        ))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Inserted data for {SYMBOL} at {latest_ts}")

    except Exception as e:
        logging.error(f"Error during fetch/store: {e}")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}
dag = DAG(
    "stock_data_pipeline",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
)

fetch_store_task = PythonOperator(
    task_id="fetch_and_store_stock_data",
    python_callable=fetch_and_store_stock_data,
    dag=dag,
)