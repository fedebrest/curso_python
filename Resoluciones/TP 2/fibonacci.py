n = int(input("ingrese un numero entero"))
f1 = 1
f2 = 1

for i in range(n):
    if i ==0:
        print(f1)
    elif (i==1):
        print(f2)
    else:
        x = f1+f2
        print(x)

        f1=f2
        f2=x
