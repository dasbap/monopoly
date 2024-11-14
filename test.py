import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

monCurseur = mydb.cursor()

monCurseur.execute("""CREATE DATABASE if not exists monopoly""")

