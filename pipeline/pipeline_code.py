import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bronze_layer import create_bronze_table
from src.silver_layer_transformation import silver_transformation
from utils.read_yaml.read_yaml import ReadYaml
from utils.spark_session.spark_class import SparkClass
from utils.silver_scd import ScdTypeTwo
from utils.arguments.arguments import args


table, load = args()

yaml_file = ReadYaml(table_name = table)
spark = SparkClass().spark


# Bronze
if load == 'FL':
    source_df = create_bronze_table(spark, table, 'FL')
else:
    source_df =  create_bronze_table(spark, table, 'CDC')
"""
Silver Layer

First Phase: Transformation
"""
df_silver_tronsformed = silver_transformation(bronze_df = source_df, name = table, yaml_file = yaml_file.read_yaml)
"""
Silver Layer

Second Phase: SCD
"""

if yaml_file.is_scd:
    if spark.catalog.tableExists(yaml_file.fetch_table_name('silver_table')):
        # Incremental Load
        scd_process = ScdTypeTwo(source_df = df_silver_tronsformed, primary_keys = yaml_file.primary_keys, non_primary_keys = yaml_file.non_primary_keys, target_table_name = yaml_file.fetch_table_name('silver_table'))

        scd_process.debug_function
        scd_process.merge_source_to_target



    else:
        # Initial Load
        source_df = ScdTypeTwo(df_silver_tronsformed, yaml_file.primary_keys, yaml_file.non_primary_keys)
        source_df.adding_scd_cols.write.mode('overwrite').saveAsTable(yaml_file.fetch_table_name('silver_table'))
