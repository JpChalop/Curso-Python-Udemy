"""
#Loop for :

#el segundo numero del rango nunca está incluido, termina justo en el anterior

for x in range(0, 101, 10): #el tercer numero es en cuantos numeros incrementa 
        print(x)

for x in range(7):
    print("estamos en el --> " + str(x))
    total +=10
    print("el total es --> " + str(total))
print("comunicado finalizado")
"""



"""
#while loop:

respuesta = "" 

while respuesta !="stop":
    respuesta= input("Ingrese un texto: ")
"""



#Loop for y while loop:

part_max= int(input("Por favor, ingrese la cantidad máxima de participantes--> "))
print("\nEl sistema ha sido configurado para aceptar",part_max,"participantes\n")

cant_part = 0

while(cant_part < part_max):
    Nombre = input("Ingrese su nombre\n")
    email = input ("Ingrese su correo electrónico\n")
    print("Hola",Nombre," su email es",email,"Desea confirmar su inscripción?\n")
    print("Para confirmar \"Si\" o para rechazar \"No\"")
    respuesta= input()
    if respuesta == "si":
        print("Gracias confirmamos su inscripción, lo esperamos!")
        print("\n\n\n")
        print("Su numero de participante es: ", cant_part)
        print("\n\n\n")
        cant_part += 1

    else: 
        print("Registro cancelado\n")

print("Cantidad máxima alcanzada")
