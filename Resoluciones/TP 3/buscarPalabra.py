numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    buscar = input("Dígame la palabra a buscar: ")
    contador = 0
    for i in lista:
        if i == buscar:
            contador += 1;
    if contador == 0:
        print("La palabra '" + buscar + "' no aparece en la lista.")
    elif contador == 1:
        print("La palabra '" + buscar + "' aparece una vez en la lista.")
    else:
        print("La palabra '" + buscar + "' aparece", contador, "veces en la lista.")
