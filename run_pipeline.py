import os

print("Starting Pipeline...")

os.system("python -m src.transformations.silver_layer")
print("Silver layer done")

os.system("python -m src.transformations.gold_layer")
print("Gold layer done")

print("Pipeline completed successfully")