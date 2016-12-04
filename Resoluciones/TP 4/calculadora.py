def multiplicar(numero1, numero2):
    resultado= numero1*numero2
    print("el resultado de la operacion seleccionada es: ", resultado)
    return 

def restar(numero1, numero2):
    resultado= numero1-numero2
    print("el resultado de la operacion seleccionada es: ", resultado)
    return     

def dividir(numero1, numero2):
    resultado= numero1//numero2
    print("el resultado de la operacion seleccionada es: ", resultado)
    return 

def sumar(numero1, numero2):
    resultado= numero1+numero2
    print("el resultado de la operacion seleccionada es: ", resultado)
    return 

#resultado=0
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))
opcion=int(input("ingrese la opción de la operación deseada: \n 1) Sumar \n 2) Restar \n 3) Multiplicar \n 4) Dividir \n"))

if opcion==1:
    sumar(numero1, numero2)
elif opcion==2:
    restar(numero1, numero2)
elif opcion==3:
    multiplicar(numero1, numero2)

elif opcion==4:
    dividir(numero1, numero2)

