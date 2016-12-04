class Becario:
    def __init__(self, nombre, legajo, beca):
        self.nombre = nombre
        self.legajo = legajo
        self.beca= beca

nombre=input("ingrese nombre del Becario: ")
legajo=input("ingrese legajo de becario: ")
beca=input("ingrese nombre de beca: ")
#x = Complejo(3.0, -4.5)
becario = Becario(nombre, legajo, beca)
print("Nombre:",becario.nombre,"\nLegajo:", becario.legajo,"\nBeca:", becario.beca)
