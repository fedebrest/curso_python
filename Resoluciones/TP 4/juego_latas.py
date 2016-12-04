def jugar(intento=1): 
    respuesta = input("ingrese cantidad de latas bajadas: ") 
    if respuesta != 10: 
        if intento < 3: 
            print ("Inténtalo de nuevo" )
            respuesta2 = input("ingrese cantidad de latas bajadas esta vez: ")
            respuesta=respuesta+respuesta2
            intento += 1 
            jugar(intento) # Llamada recursiva 
        else: 
            print ("\nPerdiste!" )
    else:
        print ("\nGanaste!")

print("Bienvenido al juego de las latas \n")        
jugar()
