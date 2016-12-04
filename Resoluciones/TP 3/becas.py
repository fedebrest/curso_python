becarios=[]
cantidad=int(input("ingrese cantidad de becarios: "))
#cantidad=3
becas=tuple()
for i in range(cantidad):
    nombre=input("ingrese el nombre del becario que desee colocar en la lista: ")
    beca=input("Ingrese el nombre de la beca del estudiante: ")
    becas=(nombre,beca)
    becarios.append(becas)
print("La lista de becarios es: ", becarios)
