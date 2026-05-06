import pandas as pd
import random

rows = 10000

products = [
    (500, "iPhone", "Electronics"),
    (501, "Laptop", "Electronics"),
    (502, "Shoes", "Fashion"),
    (503, "Watch", "Fashion")
]

customers = [
    (100, "Rahul"),
    (101, "Amit"),
    (102, "Kiran"),
    (103, "Sneha")
]

cities = ["Hyderabad", "Bangalore", "Chennai", "Delhi"]

data = []

for i in range(rows):
    product = random.choice(products)
    customer = random.choice(customers)

    data.append([
        i,
        customer[0],
        customer[1],   # customer_name
        product[0],
        product[1],    # product_name
        product[2],    # category
        random.randint(100, 2000),
        random.choice(cities)
    ])

df = pd.DataFrame(data, columns=[
    "order_id",
    "customer_id",
    "customer_name",
    "product_id",
    "product_name",
    "category",
    "amount",
    "city"
])

df.to_csv("data/bronze/orders_bronze.csv", index=False)

print("Real dataset generated")