def contarA(palabra):
    contador=0
    for i in range(len(palabra)):
        if palabra[i]=="A" or palabra[i]=="a":
            contador=contador+1
    return contador

palabra=input("ingrese una palabra: ")
cantidad=contarA(palabra)
print("la letra A aparece:",cantidad,"veces")





