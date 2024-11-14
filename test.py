import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "monopoly"
)

monCurseur = mydb.cursor()
monCurseur.execute("""CREATE TABLE IF NOT EXISTS Quartiers (
                id INT NOT NULL UNIQUE AUTO_INCREMENT,
                couleur VARCHAR(255),
                prix_maison INT NOT NULL,
                PRIMARY KEY(id)
                )
                """)
