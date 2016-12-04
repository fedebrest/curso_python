x=int(input("ingrese un numero"))
termino = x
factorial = x
while (termino >1):
    factorial = factorial * (termino -1)
    termino = termino -1
print("Factorial de", x, " = ",factorial)
