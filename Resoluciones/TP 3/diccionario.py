materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

'''for dia in materias:
   print (dia, ":", materias[dia]) '''

for dia, codigos in materias.items():
   print (dia, ":", codigos)
