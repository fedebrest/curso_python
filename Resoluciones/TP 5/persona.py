class Persona:
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print ('Nombre:')
        print (self.nombre)

persona1=Persona()
persona1.inicializar('Juan')
persona1.imprimir()

persona2=Persona()
persona2.inicializar('Ana')
persona2.imprimir()
