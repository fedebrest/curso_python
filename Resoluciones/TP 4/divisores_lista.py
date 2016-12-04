def divisorLista(lista,dividendo,lista2):
    for i in range(0,len(lista)):
        if lista[i]%dividendo == 0:
            lista2.append(lista[i])
    return lista2

lista=[]
lista2=[]
cantidad=int(input("ingrese cantidad de elemtnos de la lista: "))
for i in range(cantidad):
    numero=int(input("ingrese un numero: "))
    lista.append(numero)
dividendo=int(input("ingrese el numero de dividendo: "))

resultado=divisorLista(lista,dividendo,lista2)
print ("divisores = ", lista2)
