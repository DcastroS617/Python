import mysql.connector

##object that contains db info and opens a connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "tree_db"
)

##simple db connection object
##mydb = mysql.connector.connect(
##    host = "localhost",
##    user = "root",
##)

##cursor executes sql statements in python
cursor = mydb.cursor()

cursor.execute("SELECT * FROM families")

for x in cursor:
    print(x)