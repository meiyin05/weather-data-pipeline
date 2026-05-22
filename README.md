# Automated Weather Data Pipeline

## Overview

This project is an automated end-to-end weather data pipeline built using modern data engineering tools. The pipeline extracts real-time weather data from the Weatherstack API, transforms and models the data with dbt, orchestrates workflows using Apache Airflow, stores data in PostgreSQL, and visualizes insights through Apache Superset.

The main goal of this project is to demonstrate a scalable and automated ELT (Extract, Load, Transform) workflow for weather analytics and reporting.

---

## Tech Stack

- PostgreSQL — Data warehouse
- Weatherstack API — Weather data source
- Apache Airflow — Workflow orchestration
- dbt — Data transformation and modeling
- Apache Superset — Data visualization and dashboards
- Docker — Containerization and environment management

---

## Architecture

```text
Weatherstack API
        ↓
   Airflow DAG
        ↓
PostgreSQL (Raw Data)
        ↓
       dbt
        ↓
PostgreSQL (Transformed Data)
        ↓
  Superset Dashboard
```
## Project Structure
```text
weather-data-pipeline/
│
├── airflow/              
├── dbt/                  
├── postgres/   
├── api-request/       
├── superset/             
├── docker-compose.yml    
└── README.md
```
## Workflow
1. Data Extraction
Airflow fetches real-time weather data from the Weatherstack API on a scheduled interval.

2. Data Loading
The raw JSON response is loaded into PostgreSQL staging tables.

3. Data Transformation
dbt transforms and models the raw weather data into analytics-ready tables.

4. Visualization
Superset connects to PostgreSQL and displays dashboards for weather analysis and monitoring.


