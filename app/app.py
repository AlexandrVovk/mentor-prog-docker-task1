from flask import Flask
import mysql.connector

app = Flask(__name__)



@app.route("/")
def index():
    # return "Hello World!"
    mydb = mysql.connector.connect(
      host="mysql",
      user="root",
      password="my-secret-pw",
      database="app"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT text FROM app_table ORDER BY ID DESC LIMIT 1;")
    myresult = mycursor.fetchall()

    return myresult[0][0]
