from flask import Flask
import pyodbc

app = Flask(__name__)

host = '157.55.80.145,1702'
db = 'Bildin'
user = 'SoporteBildin'
password = 'B1LD1N*.'
port = '1702'
conected=False

try:
  conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+host+';DATABASE='+db+';UID='+user+';PWD='+ password)
  cursor = conn.cursor()
  conected=True
  print('Conexion exitosa')
except:
  print('No se pudo conectar a la base de datos')

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test")
def test():
  if conected:
    cursor.execute("EXEC [sp_ObtenerAsistentesAsamblea] 'B35E992D-34DB-43B9-A490-6D179F79B7E9', null")
    row=cursor.fetchall()
    return str(row)
  else:
    return 'No se pudo conectar a la base de datos'

if __name__ == "__main__":
  app.run()