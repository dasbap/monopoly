# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )

# monCurseur = mydb.cursor()

# monCurseur.execute("""CREATE DATABASE if not exists monopoly""")



from joueur import *
from plateau import *

joueur_1 = Vrais_Joueur()
joueur_1.ajouter_propriete(terrain[0])
print(joueur_1.proprietes)