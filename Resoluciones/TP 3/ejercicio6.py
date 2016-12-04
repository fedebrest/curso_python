# Ejercicio nº06 - Borrar Paciente

# Crear una lista de pacientes
pacientes = ["Fede", "Alan", "Emily","Yanela", "Pablo"]

nombre = input("Ingrese el nombre del paciente a eliminar: ")
cantidad = len(pacientes)
for i in range(cantidad):
    print(i)
    if (nombre == pacientes[i]):
        del pacientes[i]
        break
print(pacientes)