# Databricks notebook source
# DBTITLE 1,Cell 1
df = spark.table("workspace.bronze.store_sales_raw")

# COMMAND ----------

df.show(5)

# COMMAND ----------

# DBTITLE 1,Untitled
#Alterando os tipos das colunas

from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DecimalType, DoubleType

df = (
      df.withColumn("CustomerID", col("CustomerID").cast(IntegerType()))
      .withColumn("Age", col("Age").cast(IntegerType()))
      .withColumn("Amount", col("Amount").cast(DoubleType()))
      .withColumn("ItemRating", col("ItemRating").cast(DoubleType()))
      .withColumn("DiscountApplied%", col("DiscountApplied%").cast(DoubleType()))
      .withColumn("PreviousPurchases", col("PreviousPurchases").cast(IntegerType()))
      )

# COMMAND ----------

df.write.mode("overwrite").format("delta").saveAsTable("workspace.silver.store_sales_silver")