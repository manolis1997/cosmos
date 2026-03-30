from databricks.connect.session import DatabricksSession as SparkSession
from utils.silver_class_transformation import SilverTransformation

spark = SparkSession.builder\
    .getOrCreate()

def silver_transformation(bronze_df, name, yaml_file):
    silver_transform = SilverTransformation(source_df = bronze_df, name = name, yaml_file = yaml_file)
    df_silver = silver_transform.apply_transformations()
    return df_silver