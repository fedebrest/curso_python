lista=[]
cantidad=3
for i in range(cantidad):
    paciente=input("ingrese el nombre del paciente que desee colocar en la lista: ")
    lista.append(paciente)
    
nombre=input("ingrse el nombre del paciente que desea buscar: ")
for i in range(cantidad-1):
    if nombre == lista[i]:
        posicion=lista.index(nombre)
        print("La posicion de",nombre,"es:",posicion)
