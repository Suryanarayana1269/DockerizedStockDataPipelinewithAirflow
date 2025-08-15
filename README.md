# 🚀 Dockerized Stock Data Pipeline with Airflow

[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)]()
[![PostgreSQL](https://img.shields.io/badge/Postgres-13+-green.svg)]()
[![Airflow](https://img.shields.io/badge/Airflow-2.8+-brightgreen.svg)]()

> **Automated stock data pipeline, fully containerized, error-resilient, and ready for production analytics!**

---

## 📚 Project Overview

Fetch, process, and store stock market data on an **hourly** schedule using Apache Airflow, Python, and PostgreSQL—all orchestrated with Docker Compose.

- **Scheduled**: Runs automatically on a set interval (hourly).
- **Automated**: Airflow handles scheduling, execution, and monitoring.
- **Robust**: Comprehensive error handling and configurable parameters.
- **Secure**: Secrets (API keys, passwords) managed via environment variables.
- **Extensible**: Easily swap APIs, scale schedule, or add more tasks.

---

## 🏗️ Architecture

- **flowchart LR**
- **subgraph Airflow**
- **direction LR**
- **Scheduler -->|Triggers| DAG**
- **DAG -->|Runs| Python_Script**
- **Webserver**
- **end**
- **Python_Script -->|Upserts| Postgres[(PostgreSQL DB)]**
- **User-->Webserver**
- **Python_Script-->|"API Call"| AlphaVantage[Alpha Vantage API]**


---

## ✨ Features

- **Airflow DAG:** Defines the ETL flow; scheduled hourly.
- **Data Fetcher:** Python script gets latest data from Alpha Vantage API.
- **Database Integration:** Robust interaction with PostgreSQL.
- **Error Handling:** Catches and logs any API, parsing, or DB errors.
- **Secure Secrets:** API key, DB credentials stored in `.env` file and never in code.
- **One-command startup:** All services launched with `docker-compose up`.

---

## 🚦 Quick Start

1. **Clone the Project:** :
   ```
   git clone https://github.com/Suryanarayana1269/DockerizedStockDataPipelinewithAirflow/
   cd <your-repo-dir>
   ```

2. **Configure Environment Variables:**
- Get a free [Alpha Vantage API key](https://www.alphavantage.co/support/#api-key)
- Create a `.env` file:
  ```
  ALPHAVANTAGE_API_KEY=your_alpha_vantage_key
  STOCK_SYMBOL=MSFT      # or GOOG, AAPL, etc.
  ```

3. **Run the Pipeline:**
  ```
  docker-compose up airflow-init # One-time DB and admin creation
  docker-compose up # Launch all services

  ```


4. **Access Airflow UI:**  
[http://localhost:8080](http://localhost:8080)  
- **Username**: `airflow`
- **Password**: `airflow`

---

## 🗂️ Project Structure
```

├── dags/
│ └── stock_data_dag.py # Airflow DAG with ETL logic
├── .env # Secrets (API key, symbol)
├── docker-compose.yml # All-in-one stack launcher
├── README.md # You're reading it!

```

---

## 📝 How it Works

- **1. Scheduler** triggers the DAG on schedule.
- **2. Python task** fetches stock data from Alpha Vantage.
- **3. Data is parsed** and saved into the `stock_data` table in Postgres.
- **4. All errors** are logged; pipeline is robust to API/db downtime and missing data.

---

## ⚙️ Customization

- **Change stock**: Set `STOCK_SYMBOL` in `.env`.
- **Change schedule**: Edit `schedule_interval` in `stock_data_dag.py` (e.g. `"@daily"` for once daily).
- **Use another API**: Adjust `fetch_and_store_stock_data()` function.

---

## ✅ Requirements

- Docker & Docker Compose
- Free Alpha Vantage API key

---

## 🚑 Troubleshooting

- **Ports in use error**: Stop other Postgres/Airflow instances or change ports in `docker-compose.yml`.
- **Times in UTC**: Add `AIRFLOW__CORE__DEFAULT_TIMEZONE=Asia/Kolkata` in all Airflow service env vars for IST.
- **Viewing data**: Use DBeaver, pgAdmin, or `psql` to inspect the `stock_data` table in the database (`localhost:5432`, user/pass: `postgres`).

---

## 📈 What’s Next

- Add more stocks.
- Integrate with Grafana or Metabase for live dashboards.
- Add more sophisticated ETL tasks to the DAG.
- Deploy to cloud services with managed Airflow and Postgres.

---

## 🙏 Credits

- Built with [Apache Airflow](https://airflow.apache.org/)
- Free stock data from [Alpha Vantage](https://www.alphavantage.co/)

---

## 📮 Contact

Questions? File issues or suggestions on this repo, or email [suryanarayanabodapati1269@gmail.com](mailto:suryanarayanabodapati1269@gmail.com).

---

## 🙏 Acknowledgment

I would like to sincerely thank **8Bytes.Ai** for providing the opportunity to work on this Python Internship Technical Assessment. This project has been a valuable learning experience, allowing me to deepen my understanding of data pipelines, containerization, and orchestration with Airflow. I am grateful for this chance to develop practical skills and showcase my abilities.

---

### Screenshots & Demo Video
## Screenshots
- **Login Page**:
<img width="1900" height="873" alt="image" src="https://github.com/user-attachments/assets/9629565c-cb86-4899-a459-b96ceb8b735e" />

- **Home Page**:
<img width="1900" height="866" alt="image" src="https://github.com/user-attachments/assets/cd4f229b-cc77-4a3d-8c67-eda759aaed4b" />

- **Stock_Pipeline Page**:
<img width="1919" height="865" alt="image" src="https://github.com/user-attachments/assets/700b81a0-b912-49e5-8697-b30bde50b9b5" />

- **Cluster Activity Page**:
<img width="1914" height="864" alt="image" src="https://github.com/user-attachments/assets/1dc58aee-cf68-45a5-9256-c2f1638263a6" />

- **DAG Details Page**:
<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/3b4b109d-b515-4427-8732-9a07ad221b07" />

## Demo Video
- **Demo Video Link** : https://drive.google.com/file/d/1GksG42xqUWPXgzx4l0TBIuQT5N49EcIV/view?usp=sharing
