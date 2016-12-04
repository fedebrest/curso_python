a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

print('La receta auténtica del alioli:\n1- Sumar \n2- Restar \n3- Multiplicar \n4- Dividir \n5- Salir')
opcion=int(input("Ingrese una opcion: "))
if opcion == 1:
    resultado=a+b
    print("el resultado de la suma es",resultado)
elif opcion == 2:
    resultado=a-b
    print("el resultado de la resta es",resultado)
elif opcion == 3:
    resultado=a*b
    print("el resultado de la multiplicacion es",resultado)
elif opcion == 4:
    resultado=a//b
    print("el resultado de la division es",resultado)
elif opcion == 5:
    print("Adios!")
    exit()
else:
    print ("opcion incorrecta")
