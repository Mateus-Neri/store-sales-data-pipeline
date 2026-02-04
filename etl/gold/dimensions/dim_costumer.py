# Databricks notebook source
df = spark.table('workspace.silver.store_sales_silver')

# COMMAND ----------

dim_costumer = df.select("CustomerID","Age", "Gender", "PreviousPurchases")


# COMMAND ----------

dim_costumer = dim_costumer.withColumnRenamed("CustomerID", "customer_id") \
                .withColumnRenamed("Age", "age") \
                .withColumnRenamed("Gender", "gender") \
                .withColumnRenamed("PreviousPurchases", "previous_purchases")

# COMMAND ----------

dim_costumer.write.mode("overwrite").format("delta").saveAsTable("workspace.gold_store_sales.dim_costumer")