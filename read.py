# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teste"
)

cursor = connection.cursor()

sql = f"SELECT name FROM users Where id = ''"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)