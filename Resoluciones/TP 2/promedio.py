materias=int(input("ingrese cantidad de materias: "))
sumatoria=0
promedio=0
for i in range(materias):
    nota=int(input("ingrese la nota: "))
    sumatoria=sumatoria+nota
promedio=sumatoria/materias
print("el promedio de notas es:",promedio)
