import random

class Alumno(object):
    """
    Attributos:
        nombre: String representando el nombre del alumno.
        apellido: String representando el aperllido del alumno 
    """

    def __init__(self, nombre, apellido, legajo, beca):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.beca = beca

class Beca(object):

    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

class Main:

  def __call__(self):
    becas = []
    alumnos = []

    cant_beca=range(int(input("ingrese cantidad de alumnos: ")))
    for i in cant_beca:
    	nombre = input("Ingrese nombre becario: ")
    	apellido = input("Ingrese apellido becario: ")
    	legajo=int(input("ingrese legajo de becario: "))
    	nombreBeca = input("Ingrese nombre de la beca: ")
    	beca = Beca(str(i), nombreBeca)
    	alumno = Alumno(nombre, apellido, legajo, beca)
    	becas.append(beca)
    	alumnos.append(alumno)
    
    print('Listado de alumnos y becas')
    for i in cant_beca:
        print("\nAlumno: " + alumnos[i].nombre + ' ' + alumnos[i].apellido + '\nLegajo: ' + str(alumnos[i].legajo) + '\nBeca asignada: ' + alumnos[i].beca.nombre)

main_instance = Main()
main_instance() #this is calling the __call__ method
