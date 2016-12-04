lista=[]
#cantidad=3
cantidad=int(input("ingrese la cantidad de pacientes: "))
for i in range(cantidad):
    paciente=input("ingrese el nombre del paciente que desee colocar en la lista: ")
    lista.append(paciente)
print("El orden de atención de los pacientes será:", lista)
