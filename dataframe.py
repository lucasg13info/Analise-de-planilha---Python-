# import xlrd
# import pandas as pd
# import MySQLdb
# import mysql.connector

# # Abra a pasta de trabalho e defina a planilha
# book = pd.read_excel("pessoas.xlsx", engine='openpyxl')
# #book = xlrd.open_workbook("pessoas.xlsx", engine='openpyxl')
# sheet = book.sheet_by_name("source")

# # Establish a MySQL connection
# mydb = mysql.connect.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database='db_oi')


# # Obtenha o cursor, que é usado para percorrer o banco de dados, linha por linha
# cursor = mydb.cursor()

# # Crie a consulta INSERT INTO sql

# #query = """INSERT INTO excel (product, customer_type, rep, date, actual, expected, open_opportunities, closed_opportunities, city, state, zip, population, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
# query = "INSERT INTO excel (nome, idade, estado, altura) VALUES(%s, %s, %s, %s)"
# # Crie um loop For para iterar em cada linha do arquivo XLS, começando na linha 2 para pular os cabeçalhos
# for r in range(1, sheet.nrows):
# 		nome		= sheet.cell(r,).value
# 		idade   	= sheet.cell(r,1).value
# 		estado		= sheet.cell(r,2).value
# 		altura		= sheet.cell(r,3).value
		

# 		# Atribuir valores de cada linha
# 		values = (nome, idade, estado, altura)

# 		# Executar consulta sql
# 		cursor.execute(query, values)

# # Close the cursor
# cursor.close()

# # Commit the transaction
# mydb.commit()

# # Close the database connection
# mydb.close()

# # Print results
# print ("")
# print ("All Done! Bye, for now.")
# print ("")
# columns = str(sheet.ncols)
# rows = str(sheet.nrows)
# #print ("Acabei de importar" %2B columns %2B " colunas e " %2B rows %2B " linhas no MySQL!")




import pandas as pd
from pandas.core.frame import DataFrame
dados = pd.read_excel("pessoas.xlsx")

#DataFrame = pd.DataFrame()

dados_df = pd.DataFrame(dados)
print(dados_df)
