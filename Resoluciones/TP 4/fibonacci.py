def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


numero=int(input("ingrese un numero para calcular su fibbonaci: "))
resultado=fib(numero)
print("el resultado de la sucesión de ese término es:", resultado)
