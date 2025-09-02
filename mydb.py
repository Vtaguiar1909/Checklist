import mysql.connector 

dataBase = mysql.connector.connect(
    host = "localhost",
    user= "root",
    passwd = "Central-mangas3"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE listag")
print("All Done !")