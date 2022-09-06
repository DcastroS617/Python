from db import insert, show, searchByPk

class Hamster:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

##Insert a new hamster
def CreateHamster(hamster):
    ##%s es la forma de insertar valores evitando sql injection
    query = """INSERT INTO hamster (name, age, colour) VALUES (%s, %s, %s)"""
    ##val es el diccionario que contiene el objeto de los parametros
    val = (hamster.name, hamster.age, hamster.colour)
    insert(query, val)

def ShowHamsters():
    query = """SELECT * FROM hamster"""
    show(query)

def HamsterById(id):
    val = []
    query = """SELECT * FROM hamster WHERE Id = %s"""
    val.append(id)
    result = searchByPk(query, val)
    return result

def UpdateHamster(id):
    hamster = HamsterById(id)
    if(type(hamster) is tuple):
        query = """UPDATE hamster SET name = %s, age = %s, colour = %s WHERE Id = %s"""
        name = input("Introduce un nombre de hamster: ")
        age = input("Introduce la edad del hamster: ")
        colour = input("Introduce el color del hamster: ")
        val = (name, age, colour, id)
        ##val = (hamster[1], hamster[2], hamster[3], id)
        insert(query, val)
    else:
        print("El hamster no se encuentra en la base de datos.")

def DeleteHamster(id):
    hamster = HamsterById(id)
    if(type(hamster) is tuple):
        query = """DELETE FROM hamster WHERE Id = %s"""
        val = (id,)
        insert(query, val)
    else:
        print("El hamster no se encuentra en la base de datos.")
        
##CreateHamster(Hamster("bobby", "2", "black"))
##ShowHamsters()

##Show hamsters in db