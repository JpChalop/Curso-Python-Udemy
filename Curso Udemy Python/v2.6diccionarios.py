"""
paciente = {"nombre":"Juan", "edad":32, "peso":70.5, "fuma":False}

#Para acceder a un dato concreto:
print(paciente["nombre"])
print(paciente["fuma"])
#Forma más abreviada:
print(paciente.get("edad"))

#Con esto se saca "edad" de la lista y se guarda como "valor"
valor= paciente.pop("peso")

#Actualizas datos
paciente.update({"edad": 35})
#Forma más abreviada:
paciente["edad"]=38

#Buscar datos dentro del diccionario:
print("nombre" in paciente)

print(paciente)
"""

paciente1= {"Nombre":"Juan", "Edad":32, "Peso":70.5, "Fuma":True}
paciente2= {"Nombre":"Pedro", "Edad":23, "Peso":60.5, "Fuma":False}
paciente3 = {"Nombre":"Julia", "Edad":13, "Peso":40.5, "Fuma":False}

pacientes = [paciente1,paciente2,paciente3]

nombrex  = ["uno","dos","tres","cuatro"]
#len toma en cuenta todos los elementos del diccionario sin tener q especificar cuantos son
for x in range(len(nombrex)):
    print(nombrex[x])

for clave, valor in paciente1.items():
    print("")
    print("Clave -> ",clave," // ","Valor -> ", valor)
    print("")
    print("***********************************\n")