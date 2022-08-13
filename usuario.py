import datetime
import mysql.connector



class User:
    def __init__(self, ids=None, name=None, email=None):
        self.id = ids
        self.email = email
        self.name = name

    def save_bd(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="teste"
        )
        cursor = connection.cursor()
        sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
        data = (
            f'{self.name}',
            f'{self.email}',
            datetime.datetime.today()
        )
        cursor.execute(sql, data)
        connection.commit()
        userid = cursor.lastrowid
        print("Foi cadastrado o novo usuário de ID:", userid)
        cursor.close()
        connection.close()
    @classmethod
    def from_db(cls,id):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="teste"
        )
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

    def update(self,id,name,email):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="teste"
        )
        cursor = connection.cursor()

        sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        data = (
            f'{name}',
            f'{email}',
            f'{id}'
        )

        cursor.execute(sql, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print(recordsaffected, " registros alterados")
    def deletar(self,id):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="teste"
        )
        cursor = connection.cursor()

        sql = "DELETE FROM users WHERE id = %s"
        data = (id,)

        cursor.execute(sql, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print(recordsaffected, " registros excluídos")
    @classmethod
    def lister(cls):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="teste"
        )
        cursor = connection.cursor()

        sqls = f"SELECT * FROM users"

        cursor.execute(sqls)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        for result in results:
            print(result)