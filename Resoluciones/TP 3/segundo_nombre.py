lista=[]
cantidad=3
for i in range(cantidad):
    paciente=input("ingrese el nombre del paciente que desee colocar en la lista: ")
    lista.append(paciente)
print("El orden de atención de los pacientes será:", lista)
segundo=input("ingrese un nuevo paciente: ")
lista.insert(0,segundo)
print("El nuevo orden de atención de los pacientes será:", lista)
