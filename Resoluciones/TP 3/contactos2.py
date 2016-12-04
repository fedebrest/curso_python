contacto = ("Rafaela Carra", "Pedro", "Miguel")
telefono = ("0303456", "2616899234", "No tiene")
agenda = zip(contacto, telefono)
for nombre, valor in agenda:
    print("%s: %s" % (nombre, valor))
