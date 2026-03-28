def create_bronze_table(spark, table, load):
    if table == 'customer':
        if load == 'FL':
            return spark.createDataFrame([
                (1, 'Manolis Zacha', 'Greece', 'manolis@example.com', 250.50),
                (2, 'Teo Plat', 'Greece', 'teo@example.com', 100.00),
                (3, 'Dim Georg', 'Greece', 'dim@example.com', 75.25),
                (4, 'Dim Kourl', 'Greece', 'kourl@example.com', 300.00),
                (5, 'Kos Kourl', 'Greece', 'kos@example.com', 150.75)
            ], ["customer_id", "customer_name", "country", "email", "amount"])
        
        if load == 'CDC':
            return spark.createDataFrame([
                (1, 'Manolis Zacha', 'Greece', 'manolis@example.com', 250.50),
                (6, 'Niko Pan', 'Greece', 'niko@example.com', 120.50),
                (7, 'Elena K.', 'Greece', 'elena@example.com', 220.00),
                (2, 'Teo Plat', 'Greece', 'teo_new@example.com', 120.00),
                (4, 'Dim Kourl', 'Greece', 'kourl@example.com', 350.00)
            ], ["customer_id", "customer_name", "country", "email", "amount"])


    if table == 'product':
        if load == 'FL':
            return spark.createDataFrame([
                (10, 1, 500),
                (10, 2, 300),
                (20, 1, 150),
                (30, 3, 700),
                (20, 2, 200)
            ], ["product_id", "warehouse_id", "stock_quantity"])

        if load == 'CDC':
            return spark.createDataFrame([
                (40, 1, 100),
                (50, 2, 200),
                (10, 1, 550),
                (20, 2, 250)
            ], ["product_id", "warehouse_id", "stock_quantity"])
