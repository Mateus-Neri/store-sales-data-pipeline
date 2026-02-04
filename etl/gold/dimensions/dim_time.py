# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number


# COMMAND ----------

df = spark.table("workspace.silver.store_sales_silver")

# COMMAND ----------

dim_time = df.select("Season").distinct()

dim_time = dim_time.withColumn("time_id", row_number().over(Window.orderBy("Season")))

dim_time = dim_time.withColumnRenamed("Season", "season")


dim_time = dim_time.select("time_id", "season")

# COMMAND ----------

dim_time.write.mode("overwrite").format("delta").saveAsTable("workspace.gold_store_sales.dim_time")