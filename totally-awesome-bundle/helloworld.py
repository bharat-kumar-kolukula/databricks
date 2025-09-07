# Databricks notebook source
print("Hello World!")

# COMMAND ----------

print("Welcome to Databricks Asset Bundle")

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists work.audit;
# MAGIC Create table work.audit(
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     update_datetime timestamp default current_timestamp
# MAGIC )
