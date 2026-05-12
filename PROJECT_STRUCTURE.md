# Data Lakehouse Project — Full Structure and Contents

## Overview
This document describes the full project structure, files, and data layout for the `data-lakehouse-project` repository. It is intended as a complete shareable summary for team members or stakeholders.

---

## Repository Tree

```
data-lakehouse-project/
├── .gitignore
├── README.md
├── PROJECT_STRUCTURE.md
├── app.py
├── check_data.py
├── generate_data.py
├── requirements.txt
├── run_pipeline.py
├── dashboar.png
├── configs/
│   ├── config.json
│   └── config.yaml
├── data/
│   ├── bronze/
│   │   └── orders_bronze.csv
│   ├── gold/
│   │   ├── customer_metrics/
│   │   │   ├── _SUCCESS
│   │   │   ├── .part-00000-863ab39d-df0f-4ad2-b467-ed2b253fed67-c000.snappy.parquet.crc
│   │   │   ├── ._SUCCESS.crc
│   │   │   └── part-00000-863ab39d-df0f-4ad2-b467-ed2b253fed67-c000.snappy.parquet
│   │   └── product_metrics/
│   │       ├── _SUCCESS
│   │       ├── .part-00000-00f7f5f4-9536-4720-a201-e702365e83dc-c000.snappy.parquet.crc
│   │       ├── ._SUCCESS.crc
│   │       └── part-00000-00f7f5f4-9536-4720-a201-e702365e83dc-c000.snappy.parquet
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   └── products.csv
│   └── silver/
│       └── orders_silver/
│           ├── _SUCCESS
│           ├── .part-00000-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet.crc
│           ├── .part-00001-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet.crc
│           ├── .part-00002-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet.crc
│           ├── ._SUCCESS.crc
│           ├── part-00000-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet
│           ├── part-00001-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet
│           └── part-00002-de028b8e-9a10-4c96-a5d4-5cab563ff6d5-c000.snappy.parquet
├── src/
│   ├── __init__.py
│   ├── ingestion/
│   │   └── load_raw.py
│   ├── transformations/
│   │   ├── gold_layer.py
│   │   └── silver_layer.py
│   └── utils/
│       ├── __init__.py
│       ├── config_reader.py
│       └── logger.py
```

---

## File Summary

### Root files
- `.gitignore`
  - Ignores Python cache, compiled files, environment files, and VS Code settings.

- `README.md`
  - Contains project overview, architecture, tech stack, features, and basic run instructions.

- `PROJECT_STRUCTURE.md`
  - This document: full project structure and explanations.

- `app.py`
  - Streamlit dashboard application.
  - Loads gold parquet data from `data/gold/product_metrics` and `data/gold/customer_metrics`.
  - Displays KPIs, filters, charts, and drill-down tables.

- `check_data.py`
  - PySpark script to validate dataset layers.
  - Reads Bronze CSV, Silver parquet, and Gold parquet outputs and prints sample rows.

- `generate_data.py`
  - Data generator for Bronze data.
  - Produces 50,000 order records with customers, products, city, amount, and date.
  - Writes `data/bronze/orders_bronze.csv`.

- `run_pipeline.py`
  - Shell-style runner for the pipeline.
  - Executes Silver layer then Gold layer:
    - `python -m src.transformations.silver_layer`
    - `python -m src.transformations.gold_layer`

- `dashboar.png`
  - Dashboard preview image.

- `requirements.txt`
  - Full Python dependency list for the project.
  - Includes packages such as `pyspark`, `streamlit`, `pandas`, `apache-airflow`, `faker`, and more.

### Configuration files
- `configs/config.yaml`
  - Contains pipeline paths for data layers:
    - `raw`: `data/raw`
    - `bronze`: `data/bronze`
    - `silver`: `data/silver`
    - `gold`: `data/gold`

- `configs/config.json`
  - Contains concrete output paths used by code:
    - `bronze`: `data/bronze/orders_bronze.csv`
    - `silver`: `data/silver/orders_silver`
    - `gold_product`: `data/gold/product_metrics`
    - `gold_customer`: `data/gold/customer_metrics`

### Data files
- `data/raw/customers.csv`
- `data/raw/orders.csv`
- `data/raw/products.csv`

These are source/raw datasets used for the lakehouse pipeline.

- `data/bronze/orders_bronze.csv`
  - Bronze-layer CSV output.
  - Typical schema includes order id, customer id, customer name, product id, product name, category, amount, city, and order date.

- `data/silver/orders_silver/`
  - Silver-layer parquet output.
  - Contains cleaned and normalized order records.

- `data/gold/product_metrics/`
  - Gold-layer parquet output for aggregated product revenue metrics.
  - Includes `_SUCCESS` marker and parquet part files.

- `data/gold/customer_metrics/`
  - Gold-layer parquet output for aggregated customer order and revenue metrics.
  - Includes `_SUCCESS` marker and parquet part files.

### Source code modules
- `src/ingestion/load_raw.py`
  - Intended for loading raw input data into the pipeline.
  - Uses Pandas to read and prepare raw files.

- `src/transformations/silver_layer.py`
  - Reads Bronze CSV using Spark and the JSON config.
  - Drops duplicates and nulls.
  - Writes cleaned data to Silver parquet.

- `src/transformations/gold_layer.py`
  - Reads Silver parquet using Spark and the JSON config.
  - Aggregates product revenue and customer metrics.
  - Writes output to Gold parquet directories.

- `src/utils/config_reader.py`
  - Provides `load_config()` to read `configs/config.json`.

- `src/utils/logger.py`
  - Sets up Python logging at INFO level.

---

## Data Layer Architecture

- Raw layer: `data/raw/`
- Bronze layer: `data/bronze/orders_bronze.csv`
- Silver layer: `data/silver/orders_silver/`
- Gold layer: `data/gold/product_metrics/` and `data/gold/customer_metrics/`

---

## How to Run

Recommended pipeline run sequence:

1. Generate Bronze data:
   - `python generate_data.py`

2. Run the Silver transformation:
   - `python -m src.transformations.silver_layer`

3. Run the Gold transformation:
   - `python -m src.transformations.gold_layer`

4. Optionally run the pipeline wrapper:
   - `python run_pipeline.py`

5. View dashboard:
   - `streamlit run app.py`

6. Check data layers:
   - `python check_data.py`

---

## Notes

- The gold and silver outputs are stored as Spark parquet directories with part files and `_SUCCESS` markers.
- The repository includes a Streamlit dashboard for analytics visualization.
- The pipeline is configured through `configs/config.json` and can be extended with additional layers or sources.
