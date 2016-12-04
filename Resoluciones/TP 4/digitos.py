def sumar_dig(n):
    if n==0:
        return n
    else:
        return sumar_dig(n//10)+(n%10)

numero=int(input("ingrese el numero para calcular la sumatoria de sus digitos: "))
resultado=sumar_dig(numero)
print("la sumatoria de los",numero,"primeros terminos es:",resultado)
