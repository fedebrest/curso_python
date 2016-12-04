class Vehiculo():
 ruedas = 2
 
 def __init__(self, marca, modelo):
 self.marca = marca
 self.modelo = modelo
 
 def acelerar(self):
 pass
 
 def frenar(self):
 pass
 
class Moto(Vehiculo):
 pass
class Coche(Vehiculo):
 pass
