numero1=int(input("ingrese el rango menor: "))
numero2=int(input("ingrese el rango mayor: "))
total = 0
for i in range(numero1,numero2):
    if (i % 2) != 0:
        total += i
    i+=1
print(total)
