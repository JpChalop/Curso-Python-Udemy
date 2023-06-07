age= int(input("cuál es tu edad? --> "))
age_limit = 18

if age < age_limit:
    print("\nNo tiene permitido ingresar a este sitio.")
    print("crece amiguito \n")

if age >= age_limit:
    print("\npodés pasar capo \n")

"""
70% helado
20% pastel
10% flan
"""
stock = input("Ingrese el postre encontrado---> ")

if stock == "helado":
    print("recuerda comprar cucharas descartables")
elif stock == "pastel":
    print("recuerda comprar platos descartables")
elif stock == "flan":
    print("recuerda comprar caramelo")
else:
    print("eso no es lo que te pidieron ")
