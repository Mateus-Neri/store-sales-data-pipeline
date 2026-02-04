# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# COMMAND ----------

df = spark.table("workspace.silver.store_sales_silver")


# COMMAND ----------

# DBTITLE 1,Untitled
dim_payment = df.select("PaymentMethod").distinct()
dim_payment = dim_payment.withColumn("payment_id", row_number().over(Window.orderBy("PaymentMethod"))).withColumnRenamed("PaymentMethod", "payment_method")
dim_payment = dim_payment.select("payment_id", "payment_method")


# COMMAND ----------

dim_payment.write.mode("overwrite").format("delta").saveAsTable("workspace.gold_store_sales.dim_payment")