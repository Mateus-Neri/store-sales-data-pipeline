# Databricks notebook source
path = '/Volumes/workspace/bronze/store_sales/store_sales.csv'

df = spark.read.option("header", True).csv(path)

df = df.withColumnRenamed('DiscountApplied(%)', 'DiscountApplied%')

df.show(5)

# COMMAND ----------

# DBTITLE 1,Untitled
df.write.mode("overwrite").format("delta").saveAsTable("workspace.bronze.store_sales_raw")