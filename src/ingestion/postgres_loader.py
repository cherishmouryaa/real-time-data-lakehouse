import psycopg2
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="data_lakehouse",
    user="postgres",
    password="kandanuru",
    port="5432"
)

cur = conn.cursor()

# --------------------------
# INSERT CUSTOMERS
# --------------------------

for customer_id in range(1, 101):
    customer_name = fake.name()

    cur.execute("""
        INSERT INTO customers (customer_id, customer_name)
        VALUES (%s, %s)
    """, (customer_id, customer_name))

# --------------------------
# INSERT PRODUCTS
# --------------------------

products = [
    (1, "iPhone", "Electronics"),
    (2, "Laptop", "Electronics"),
    (3, "Shoes", "Fashion"),
    (4, "Watch", "Fashion"),
    (5, "Headphones", "Electronics")
]

for product in products:
    cur.execute("""
        INSERT INTO products (product_id, product_name, category)
        VALUES (%s, %s, %s)
    """, product)

# --------------------------
# INSERT ORDERS
# --------------------------

cities = ["Hyderabad", "Bangalore", "Chennai", "Delhi"]

for order_id in range(1, 5001):

    customer_id = random.randint(1, 100)
    product_id = random.randint(1, 5)

    amount = random.randint(500, 50000)

    city = random.choice(cities)

    order_date = fake.date_between(
        start_date="-90d",
        end_date="today"
    )

    cur.execute("""
        INSERT INTO orders (
            order_id,
            customer_id,
            product_id,
            amount,
            city,
            order_date
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        order_id,
        customer_id,
        product_id,
        amount,
        city,
        order_date
    ))

# Commit changes
conn.commit()

print("Data inserted successfully!")

cur.close()
conn.close()