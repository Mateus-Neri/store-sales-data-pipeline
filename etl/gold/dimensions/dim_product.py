# Databricks notebook source
from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

df = spark.table("workspace.silver.store_sales_silver")

# COMMAND ----------

dim_product = df.select("ItemPurchased", "Category").distinct().orderBy("ItemPurchased")

dim_product = dim_product.withColumnRenamed("Category", "category").withColumnRenamed("ItemPurchased", "item_purchased")

# COMMAND ----------

dim_product = dim_product.withColumn("product_id", row_number().over(Window.orderBy("item_purchased")))

dim_product = dim_product.select("product_id", "item_purchased", "category")

# COMMAND ----------

dim_product.write.mode("overwrite").format("delta").saveAsTable("workspace.gold_store_sales.dim_product")