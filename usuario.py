import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="teste"
)

class User:
    def __init__(self, ids=None, name=None, email=None):
        self.id = ids
        self.email = email
        self.name = name


    @classmethod
    def from_db(cls,id):
        query = f"SELECT id,name,email FROM teste.users where id = '{id}';"
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        lista=[]
        for r in row:
            lista.append(r)
        return User(lista[0],lista[1],lista[2])
