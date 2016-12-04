def invertir(list):
    if len(list)==1:
        return list
    else:
        return list[-1]+invertir(list[:-1])

a=input("ingrese un numero: ")
resultado=invertir(a)

print("El numero invertido es: ",resultado)
