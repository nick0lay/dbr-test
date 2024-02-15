import os

print("Task 1: Hello World!")

db_name = os.getenv("DB_NAME")
prefix = os.getenv("PREFIX")
print("Db name: ", db_name)
print("Prefix: ", prefix)