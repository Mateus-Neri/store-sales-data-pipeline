# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# COMMAND ----------

#Importando dimensões

dim_time = spark.table("workspace.gold_store_sales.dim_time")

dim_payment = spark.table("workspace.gold_store_sales.dim_payment")

dim_product = spark.table("workspace.gold_store_sales.dim_product")

dim_costumer = spark.table("workspace.gold_store_sales.dim_costumer")

df_sales = spark.table("workspace.silver.store_sales_silver")

# COMMAND ----------

#Joins FK
fact = (df_sales.join(dim_costumer.select("customer_id"), df_sales.CustomerID == dim_costumer.customer_id, "left"))
fact = (fact.join(dim_product.select("product_id", "item_purchased", "category"), (fact.ItemPurchased == dim_product.item_purchased) & (fact.Category == dim_product.category), "left"))
fact = (fact.join(dim_payment.select("payment_id", "payment_method"), fact.PaymentMethod == dim_payment.payment_method, "left"))
fact = (fact.join(dim_time.select("time_id", "season"), fact.Season == dim_time.season, "left"))

#Criando PK
fact = fact.withColumn("sale_id", row_number().over(Window.orderBy("customer_id")))

# COMMAND ----------

fact_sales = fact.select("sale_id", "customer_id", "product_id", "time_id", "payment_id", "Amount", "ItemRating", "DiscountApplied%").withColumnRenamed("Amount", "amount").withColumnRenamed("ItemRating", "item_rating").withColumnRenamed("DiscountApplied%", "discount_applied_pct")

# COMMAND ----------

fact_sales.write.mode("overwrite").format("delta").saveAsTable("workspace.gold_store_sales.fact_Sales")