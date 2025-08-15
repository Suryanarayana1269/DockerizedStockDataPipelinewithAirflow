# Dockerized Stock Data Pipeline

## Overview

Fetches stock data from Alpha Vantage on a set schedule via Apache Airflow and stores it in a PostgreSQL DB.

## Prerequisites

- Docker + Docker Compose
- Alpha Vantage API key

## Getting Started

1. Clone the project and enter folder.
2. Create `.env` with your API key and desired stock symbol.
3. Start services:
4. Visit Airflow UI at [http://localhost:8080](http://localhost:8080) (default creds: airflow/airflow).
5. PostgreSQL is available at localhost:5432, DB `stocks`, user/password both `postgres`.

## How it Works

- Airflow runs a DAG every hour to pull and store data.
- Data lands in a table `stock_data`.

## Stop the Pipeline

