import mysql.connector

def establishconnection(): 
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "HamsterDB"
    )
    ##el cursor se encarga de declarar el codigo sql executable
    ##cursor = mydb.cursor()
    return mydb

##metodo encargado de realizar acciones que necesitan commit
def insert(query, body):
    try:
        with establishconnection() as myconnection:
            with myconnection.cursor() as cursor:
                cursor.execute(query, body)
                myconnection.commit()
                print("query executed succesfully.")
    except mysql.connector.Error as e:
        print(e)

##metodo encargado de realizar acciones de muestra
def show(query):
    try:
        with establishconnection() as myconnection:
            with myconnection.cursor() as cursor:
                cursor.execute(query)
                for x in cursor:
                    print(x)
                print("query executed succesfully.")
    except mysql.connector.Error as e:
        print(e)
    
def searchByPk(query, body):
    try:
        with establishconnection() as myconnection:
            with myconnection.cursor() as cursor:
                cursor.execute(query, body)
                result = cursor.fetchone()
                return result
    except mysql.connector.Error as e:
        print(e)



