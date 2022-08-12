# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

import main

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teste"
)
class Create():

  cursor = connection.cursor()
  sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
  obj = main.save()
  name = obj.name
  email = obj.email
  data = (
  f'{name}',
  f'{email}',
  datetime.datetime.today()
  )

  cursor.execute(sql, data)
  connection.commit()

  userid = cursor.lastrowid

  cursor.close()
  connection.close()

  print("Foi cadastrado o novo usuário de ID:", userid)
