def sumar(n):
  if 1 == n:
    return 1
  else:
    return n + sumar( n - 1 )

numero=int(input("ingrese el numero para sumar los n primeros terminos: "))
resultado=sumar(numero)
print("la sumatoria de los",numero,"primeros terminos es:",resultado)
