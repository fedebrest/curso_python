def sumarLista(lista):
    sum=0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum

lista=[]
cantidad=int(input("ingrese cantidad de elemtnos de la lista: "))
for i in range(cantidad):
    numero=int(input("ingrese un numero: "))
    lista.append(numero)

print ("Suma = " + str(sumarLista(lista)))
