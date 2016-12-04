lista=[]
cantidad=3
for i in range(cantidad):
    paciente=input("ingrese algo para colocar en la lista: ")
    lista.append(paciente)

for i in range(len(lista)-1, -1, -1):
    print(lista[i], end=" ")

