print("")
print(" __________________________________________________________ ")
print("| Bienvenido al sistema de historias clínicas del hospital |")
print("|__________________________________________________________|")
print("")

# **********************
# * VARIABLES GLOBALES *
# **********************
running = True
database = list()


# **********************
# *     FUNCIONES      *
# **********************

def show_menu():
    print("")     
    print("\t\t»»   1 - Cargar paciente")
    print("\t\t»»   2 - Buscar paciente")
    print("\t\t»»   3 - Listar pacientes")
    print("\t\t»»   4 - Salir") 
    print("")
    res = input("Ingrese una opción » ")
    return res



# **********************
# *   LOOP PRINCIPAL   *
# **********************
while running:
    response = show_menu()
    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4: