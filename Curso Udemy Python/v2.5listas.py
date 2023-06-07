#siempre que estén separados por comas, los datos pueden ser de cualquier tipo
sabores = ["chocolate","vainilla","crema americana",2,False,2.4]
sabores2 = ["vainilla", "dulce de leche"]

sabores.extend(sabores2)
sabor_eliminado = sabores.pop(1)
print(sabor_eliminado)
print(sabores[1])

sabores.append("esto es el ultimo elemento")
sabores.insert(0,"objeto insertado")
sabores.remove("vainilla")
print(sabores[5])
print(sabores)

