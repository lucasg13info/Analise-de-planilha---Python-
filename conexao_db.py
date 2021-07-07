import mysql.connector

def insertBanco():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='db_oi')

  cursor = mydb.cursor()

  #Criando o banco de dados
    #cursor.execute("CREATE DATABASE mydatabaseTeste4")

  #Inserindo os dados abaixo no banco
  sql = "INSERT INTO email (de, para) VALUES(%s, %s)"
  val = ('luuuucccasestefano@gmail.com.br', 'Insert banco de dados')

  cursor.execute(sql, val)
  mydb.commit()

  print(cursor.rowcount, "Record inserted")

insertBanco()