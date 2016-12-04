class Complejo:
    def __init__(self, partereal, parteimaginaria):
        self.r = partereal
        self.i = parteimaginaria + "i"

parteReal=input("ingrese parte real: ")
parteImaginaria=input("ingrese parte imaginaria: ")
#x = Complejo(3.0, -4.5)
x = Complejo(parteReal, parteImaginaria)
print(x.r, x.i)
