import pandas as pd
import mysql.connector
#1
# x = pd.read_excel("pessoas.xlsx", usecols=[10, 11])

#2
x = pd.read_excel("pessoas.xlsx")
#oi = pd.read_excel("oi.xlsx", usecols=[10])
dados = [x]
print(dados)



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
  sql = "INSERT INTO excel (nome, idade, estado, altura) VALUES(%s, %s, %s, %s)"
  val = (cursor)

  cursor.execute(sql, val)
  mydb.commit()

  print(cursor.rowcount, "Record inserted")

insertBanco()