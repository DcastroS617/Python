import hamster

condicionMenu = True
print("Bienvenido a la base de datos de hamsters...")

while(condicionMenu):
    condicionSalida = True
    print("Menú Principal!")
    print("1. Insertar Hamsters.")
    print("2. Mostrar Hamsters.")
    print("3. Mostrar Hamster por ID.")
    print("4. Actualizar Hamster.")
    print("5. Eliminar Hamster.")
    print("6. Salir.")
    opcion = input("Escoge una opción: ")
    if(opcion == "1"):
        while(condicionSalida):
            name = input("Introduce un nombre de hamster: ")
            age = input("Introduce la edad del hamster: ")
            colour = input("Introduce el color del hamster: ")
            hamster.CreateHamster(hamster.Hamster(name, age, colour))
            salida = input("Desea introducir uno mas? (s/n): ")
            if(salida == "n"): 
                condicionSalida = False
    elif(opcion == "2"):
        while(condicionSalida):
            hamster.ShowHamsters()
            condicionSalida = False
    elif(opcion == "3"):
        while(condicionSalida):
            hamster.ShowHamsters()
            id = input("Inserte el ID del hamster: ")
            print(hamster.HamsterById(id))
            condicionSalida = False
    elif(opcion == "4"):
        while(condicionSalida):
            hamster.ShowHamsters()
            id = input("Inserte el ID del hamster: ")
            hamster.UpdateHamster(id)
            condicionSalida = False
    elif(opcion == "5"):
        while(condicionSalida):
            hamster.ShowHamsters()
            id = input("Inserte el ID del hamster: ")
            hamster.DeleteHamster(id)
            condicionSalida = False
    else:
        print("Que le vaya bien!!")
        break

