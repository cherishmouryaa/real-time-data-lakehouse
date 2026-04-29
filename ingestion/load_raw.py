import pandas as pd

orders = pd.read_csv('data/raw/orders.csv')

customers = pd.read_csv('data/raw/customers.csv')

merged = orders.merge(
    customers,
    on='customer_id'
)

merged.to_csv(
    'data/bronze/orders_bronze.csv',
    index=False
)

print("Bronze Layer Loaded")