def factorial(numero):
    if(numero == 0 or numero == 1):
        return 1
    else:
        return numero * factorial(numero-1)

numero=int(input("ingrese un numero para calcular su factorial: "))
resultado=factorial(numero)
print("el resultado es:", resultado)
