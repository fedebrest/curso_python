texto=input("ingrese un texto separado por espacios: ")
contador = 1

for letra in texto:
    if letra == " ":
        contador = contador +1
        
print("son", contador,"palabras")
