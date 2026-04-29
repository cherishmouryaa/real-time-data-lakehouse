import sys
import os
import pandas as pd

sys.path.append(
os.path.dirname(
os.path.dirname(
os.path.abspath(__file__)
))
)

from utils.logger import logger

logger.info("Pipeline started")

orders = pd.read_csv(
'../data/raw/orders.csv'
)

customers = pd.read_csv(
'../data/raw/customers.csv'
)

merged = orders.merge(
customers,
on='customer_id'
)

merged.to_csv(
'../data/bronze/orders_bronze.csv',
index=False
)

logger.info("Bronze layer loaded")