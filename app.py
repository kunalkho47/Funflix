from flask import Flask, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    user="avnadmin",
    password="AVNS_GfR7Y0J3xBMWVcIXRlw",
    host="mysql-21808376-kunalkhobragade0405-5360.b.aivencloud.com",
    port=27075,
    database="imdb"
)

@app.route("/", methods=["GET"])
def home():
    return "Hello, World!!"

@app.route("/genre", methods=["GET"])
def genre():
    data = request.get_json()
    query = "SELECT * FROM imbd where INSTR(genre,'"+data["genre"]+"');"
    cursor  = mydb.cursor()
    cursor.execute(query) 
    rows = cursor.fetchall()
    mydb.commit()
    return rows

@app.route("/most-liked", methods=["GET"])
def most_liked():
    query = "SELECT * FROM imbd where rating > 8;"
    cursor  = mydb.cursor()
    cursor.execute(query) 
    rows = cursor.fetchall()
    mydb.commit()
    return rows

@app.route("/most-votes", methods=["GET"])
def most_votes():
    query = "SELECT * FROM imbd where REPLACE(votes, ',', '') > 1100000;"
    cursor  = mydb.cursor()
    cursor.execute(query) 
    rows = cursor.fetchall()
    mydb.commit()
    return rows

@app.route("/Drama", methods=["GET"])
def Drama():
     query = "SELECT * FROM imbd where INSTR(genre,'Drama');"
     cursor  = mydb.cursor()
     cursor.execute(query) 
     rows = cursor.fetchall()
     mydb.commit()
     return rows

@app.route("/comedy", methods=["GET"])
def comedy():
     query = "SELECT * FROM imbd where INSTR(genre,'comedy');"
     cursor  = mydb.cursor()
     cursor.execute(query) 
     rows = cursor.fetchall()
     mydb.commit()
     return rows

@app.route("/crime", methods=["GET"])
def crime():
     query = "SELECT * FROM imbd where INSTR(genre,'crime');"
     cursor  = mydb.cursor()
     cursor.execute(query) 
     rows = cursor.fetchall()
     mydb.commit()
     return rows

@app.route("/quick-snacks", methods=["GET"])
def Quick_snacks():
    query = "SELECT * FROM imbd where duration < 90;"
    cursor  = mydb.cursor()
    cursor.execute(query) 
    rows = cursor.fetchall()
    mydb.commit()
    return rows

app.run(host='0.0.0.0', port=5000)

