# Databricks notebook source
print("Hello World!")


# COMMAND ----------

print("What is your name")

# COMMAND ----------

notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split('/')[-1]
print(notebook_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC declare or replace i int default 0;
# MAGIC DECLARE OR REPLACE VARIABLE notebook_name STRING DEFAULT 'helloworld.py';
# MAGIC set var i= (select coalesce(max(id),0) as Max_Id from work.audit);
# MAGIC set var i=i+1;
# MAGIC
# MAGIC
# MAGIC SET VAR notebook_name = notebook_name;
# MAGIC
# MAGIC INSERT INTO work.audit (id, name, update_datetime)
# MAGIC VALUES (i, notebook_name, current_timestamp);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from work.audit order by id desc
