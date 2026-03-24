# Databricks notebook source

from databricks.connect.session import DatabricksSession as SparkSession

spark = spark = SparkSession.builder\
    .getOrCreate()

# COMMAND ----------

dbutils.widgets.text("table_name", "", "")

# COMMAND ----------

table_name = dbutils.widgets.get("table_name")

# COMMAND ----------

print(table_name)

# COMMAND ----------



# # COMMAND ----------

# from pyspark.sql import Row

# data_changes = [
#     Row(customer_id=1, customer_name='Manolis Zacha', country='Greece', email='manolis@example.com', amount=300.00),
#     Row(customer_id=2, customer_name='Teo Platon', country='Greece', email='teo@example.com', amount=100.00),
#     Row(customer_id=6, customer_name='Anna Kosta', country='Greece', email='anna@example.com', amount=200.00),
#     Row(customer_id=7, customer_name='Nikos Pappas', country='Greece', email='nikos@example.com', amount=180.00),
# ]

# customers_orders_df = spark.createDataFrame(data_changes)

# customers_orders_df.show()

# # COMMAND ----------

