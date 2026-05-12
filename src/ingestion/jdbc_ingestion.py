from pyspark.sql import SparkSession

# Create Spark session with PostgreSQL JDBC driver
spark = SparkSession.builder \
    .appName("PostgreSQL JDBC Ingestion") \
    .config(
        "spark.jars",
        "drivers/postgresql-42.7.5.jar"
    ) \
    .getOrCreate()

# PostgreSQL connection properties
jdbc_url = "jdbc:postgresql://localhost:5432/data_lakehouse"

properties = {
    "user": "postgres",
    "password": "kandanuru",
    "driver": "org.postgresql.Driver"
}

# Read orders table
orders_df = spark.read.jdbc(
    url=jdbc_url,
    table="orders",
    properties=properties
)

# Show sample data
orders_df.show(10)

# Write Bronze parquet
orders_df.write.mode("overwrite").parquet(
    "data/bronze/orders_bronze_parquet"
)

print("JDBC ingestion completed!")

spark.stop()