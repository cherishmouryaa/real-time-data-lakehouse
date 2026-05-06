from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Check Data").getOrCreate()

print("\n--- BRONZE DATA ---")
df1 = spark.read.csv("data/bronze/orders_bronze.csv", header=True)
df1.show(5)

print("\n--- SILVER DATA ---")
df2 = spark.read.parquet("data/silver/orders_silver")
df2.show(5)

print("\n--- GOLD PRODUCT ---")
df3 = spark.read.parquet("data/gold/product_metrics")
df3.show(5)

print("\n--- GOLD CUSTOMER ---")
df4 = spark.read.parquet("data/gold/customer_metrics")
df4.show(5)

spark.stop()