# Real-Time Data Lakehouse Platform
## 📊 Dashboard Preview

![Dashboard](dashboard.png)
## Overview
Production-style Data Engineering project using:

Bronze -> Silver -> Gold

## Tech Stack
- Python
- Pandas
- PySpark
- Airflow
- Kafka
- PostgreSQL

## Completed
- Raw ingestion pipeline
- Bronze layer created

## Coming Next
- Silver transformations
- Gold analytics layer
- Streaming pipeline

# Data Lakehouse Project using PySpark

## 📌 Overview
This project demonstrates a complete data pipeline using PySpark with a multi-layer architecture (Bronze, Silver, Gold).

## 🏗️ Architecture
- Bronze Layer: Raw data ingestion
- Silver Layer: Data cleaning and transformation
- Gold Layer: Business-level aggregations

## ⚙️ Technologies Used
- Python
- PySpark
- Hadoop (winutils)
- Logging (custom logger)
- JSON Config-based pipeline

## 📂 Project Structure
## 🚀 How to Run

```bash
python -m src.transformations.silver_layer
python -m src.transformations.gold_layer

# Data Lakehouse Project

## Overview
Built an end-to-end data engineering pipeline using PySpark with Bronze, Silver, Gold architecture.

## Features
- Data ingestion from CSV (Bronze layer)
- Data cleaning and transformation (Silver layer)
- Aggregated business metrics (Gold layer)
- Realistic dataset (10,000+ records)
- Interactive dashboard using Streamlit

## Tech Stack
- Python
- PySpark
- Pandas
- Streamlit

## Pipeline Flow
Raw Data → Bronze → Silver → Gold → Dashboard

## Key Metrics
- Product revenue
- Customer order count

## How to Run
python generate_data.py  
python run_pipeline.py  
streamlit run app.py

# 🚀 Data Lakehouse Project (PySpark + Streamlit)

## 📌 Overview
Built an end-to-end data engineering pipeline using PySpark with Bronze, Silver, Gold architecture.

## ⚙️ Tech Stack
- Python
- PySpark
- Pandas
- Streamlit
- Faker (data generation)

## 🏗 Architecture
Raw Data → Bronze → Silver → Gold → Dashboard

## 📊 Features
- 50,000+ realistic data records
- 1000+ customers
- Product analytics (revenue, categories)
- Customer analytics (orders, revenue)
- Interactive dashboard (filters, drill-down)

## 📂 Project Structure
- Bronze → Raw data
- Silver → Cleaned data
- Gold → Aggregated metrics

## ▶️ How to Run

```bash
python generate_data.py
python -m src.transformations.silver_layer
python -m src.transformations.gold_layer
streamlit run app.py

## 🔗 Live Demo
https://your-app.streamlit.app