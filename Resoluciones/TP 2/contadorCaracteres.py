cadena = input("ingrese una cadena ")
caracter = input("ingrese una letra ")
#print("la letra",caracter,"aparece",cadena.count(caracter),"veces")
contador = 0

for letra in cadena:
    if letra == caracter:
        contador = contador +1
        
print("la letra",caracter,"aparece",contador,"veces")
