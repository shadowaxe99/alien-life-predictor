```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from schemas import AstronomicalDataSchema, ProcessedDataSchema

# Initialize Spark Session
spark = SparkSession.builder.appName("AI Alien Life Predictor").getOrCreate()

def preprocess_data():
    # Load the raw astronomical data
    astronomical_data = spark.read.format("csv").option("header", "true").schema(AstronomicalDataSchema).load("data/astronomical_data.csv")

    # Clean the data
    cleaned_data = astronomical_data.dropna()

    # Select relevant features for the machine learning model
    feature_columns = ["stellar_radius", "stellar_mass", "orbital_period", "planet_radius", "planet_mass", "surface_temperature"]
    for col_name in feature_columns:
        cleaned_data = cleaned_data.withColumn(col_name, col(col_name).cast("Float"))

    # Assemble the features into a single vector
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    processed_data = assembler.transform(cleaned_data)

    # Save the preprocessed data
    processed_data.write.format("parquet").save("data/processed_data.parquet")

    return processed_data
```