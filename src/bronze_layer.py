from databricks.connect.session import DatabricksSession as SparkSession

spark = spark = SparkSession.builder\
    .getOrCreate()

spark.sql("""
    CREATE TABLE IF NOT EXISTS mz_catalog.mz_schema.bronze_customers_orders (
    customer_id INT,
    customer_name STRING,
    country STRING,
    email STRING,
    amount DOUBLE)
USING DELTA"""
)


# spark.sql("""INSERT INTO mz_catalog.mz_schema.bronze_customers_orders (customer_id, customer_name, country, email, amount) VALUES
# (1, 'Manolis Zacha', 'Greece', 'manolis@example.com', 250.50),
# (2, 'Teo Plat', 'Greece', 'teo@example.com', 100.00),
# (3, 'Dim Georg', 'Greece', 'dim@example.com', 75.25),
# (4, 'Dim Kourl', 'Greece', 'kourl@example.com', 300.00),
# (5, 'Kos Kourl', 'Greece', 'kos@example.com', 150.75)""")


spark.sql("""CREATE TABLE IF NOT EXISTS mz_catalog.mz_schema.bronze_products_inventory (
    product_id INT,
    warehouse_id INT,
    stock_quantity INT
    )
USING DELTA""")

# spark.sql("""INSERT INTO mz_catalog.mz_schema.bronze_products_inventory (product_id, warehouse_id, stock_quantity) VALUES
# (10, 1, 500),
# (10, 2, 300),
# (20, 1, 150),
# (30, 3, 700),
# (20, 2, 200);""")