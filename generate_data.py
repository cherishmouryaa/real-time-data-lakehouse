import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------
NUM_ROWS = 50000        # total orders
NUM_CUSTOMERS = 1000    # total customers

# -----------------------------
# PRODUCT CATALOG (fixed)
# -----------------------------
products = [
    (500, "iPhone 14", "Electronics"),
    (501, "Dell Laptop", "Electronics"),
    (502, "Sony Headphones", "Accessories"),
    (503, "Nike Shoes", "Fashion"),
    (504, "Titan Watch", "Fashion"),
]

# -----------------------------
# GENERATE CUSTOMERS
# -----------------------------
customers = []

for i in range(NUM_CUSTOMERS):
    customers.append({
        "customer_id": 1000 + i,
        "customer_name": fake.name(),
        "city": fake.city()
    })

# -----------------------------
# DATE RANGE (1 year data)
# -----------------------------
start_date = datetime(2023, 1, 1)

# -----------------------------
# GENERATE ORDERS
# -----------------------------
data = []

for i in range(1, NUM_ROWS + 1):

    product = random.choice(products)
    customer = random.choice(customers)

    order_date = start_date + timedelta(days=random.randint(0, 365))

    data.append([
        i,                              # order_id
        customer["customer_id"],
        customer["customer_name"],
        product[0],                     # product_id
        product[1],                     # product_name
        product[2],                     # category
        round(random.uniform(100, 5000), 2),  # amount
        customer["city"],
        order_date.strftime("%Y-%m-%d") # date
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data, columns=[
    "order_id",
    "customer_id",
    "customer_name",
    "product_id",
    "product_name",
    "category",
    "amount",
    "city",
    "order_date"
])

# -----------------------------
# SAVE TO BRONZE
# -----------------------------
df.to_csv("data/bronze/orders_bronze.csv", index=False)

print("✅ Realistic large dataset generated successfully!")