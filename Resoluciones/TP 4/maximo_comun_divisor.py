def mcd(a, b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)

a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
resultado=mcd(a,b)
print("el Maximo Comun Divisor de",a,"y",b,"es:",resultado)
