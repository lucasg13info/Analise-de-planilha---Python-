import mysql.connector
import pandas as pd
from pandas.core.frame import DataFrame

def insertBanco():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='db_oi')

  cursor = mydb.cursor()

  #Criando o banco de dados
    #cursor.execute("CREATE DATABASE mydatabaseTeste4")

  dados = pd.read_excel("pessoas.xlsx")
  dados_df = pd.DataFrame(dados)

  #Linha1
  nome1 = str(dados_df.loc[0, 'nome'])
  idade1 = int(dados_df.loc[0, 'idade']) 
  estado1 = str(dados_df.loc[0, 'estado'])
  altura1= float(dados_df.loc[0, 'altura'])
  
  
  #Inserindo os dados abaixo no banco
  sql = "INSERT INTO excel (nome, idade, estado, altura) VALUES(%s, %s, %s, %s)"
  val = (nome1,idade1,estado1,altura1)

  cursor.execute(sql, val)
  mydb.commit()

  
  print(cursor.rowcount, "Sucesso na gravação!")
  print(f'os dados gravados foram: {nome1} {idade1} {estado1} {altura1}')

insertBanco()










