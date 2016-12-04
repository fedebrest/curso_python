def division(a, b):
    if b>a:
        return 0
    else:
        return division(a-b, b)+1


a=int(input("ingrese un numero: "))
b=int(input("ingrese otro numero: "))
resultado=division(a,b)

print("la division de esos 2 numeros es: ",resultado)
