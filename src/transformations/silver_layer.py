from src.utils.config_reader import load_config
from src.utils.logger import logger

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Load config
config = load_config()

# Initialize Spark
spark = SparkSession.builder \
    .appName("Silver Layer Processing") \
    .getOrCreate()

logger.info("Spark session started")

# Read Bronze Data using config
df = spark.read.csv(
    config["paths"]["bronze"],
    header=True,
    inferSchema=True
)

logger.info("Bronze data loaded")

# Data Cleaning
df_clean = df.dropDuplicates()
df_clean = df_clean.dropna()

# Select relevant columns
df_clean = df_clean.select(
    col("order_id"),
    col("customer_id"),
    col("customer_name"),
    col("product_id"),
    col("product_name"),
    col("category"),
    col("amount"),
    col("city")
)
logger.info("Data cleaned")

# Write Silver Layer using config
df_clean.write.mode("overwrite").parquet(
    config["paths"]["silver"]
)

logger.info("Silver layer written")

spark.stop()