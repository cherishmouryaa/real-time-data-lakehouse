from src.utils.config_reader import load_config
from src.utils.logger import logger

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

# Load config
config = load_config()

spark = SparkSession.builder \
    .appName("Gold Layer Transformation") \
    .getOrCreate()

logger.info("Gold layer started")

# Read silver data using config
df = spark.read.parquet(config["paths"]["silver"])

# Product revenue
df_product = df.groupBy("product_id", "product_name", "category") \
    .agg(sum("amount").alias("total_revenue"))


# Customer orders
df_customer = df.groupBy("customer_id", "customer_name", "city") \
    .agg(
        count("*").alias("total_orders"),
        sum("amount").alias("total_revenue")
    )
# Write gold layer using config
df_product.write.mode("overwrite").parquet(config["paths"]["gold_product"])
df_customer.write.mode("overwrite").parquet(config["paths"]["gold_customer"])

logger.info("Gold layer created successfully")

spark.stop()