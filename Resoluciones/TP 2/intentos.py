import random
n=random.randint(1, 3)
#intentos=10
#for i in range(intentos):
x=int(input("ingrese un numero"))
while x != n:
    print("vuelva a intentar")
    x=int(input())
if (x==n):
    print("adivinaste!")
#    if ingreso == n:
#        print("acertado")
#    else:
#        print("vuelva a intentar")
