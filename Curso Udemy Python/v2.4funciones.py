#función simple xq no recibe ni devuelve ningún parámetro:
def cálculo1():
    operación2 = 2 * 4 + 20
    operación2 = operación2 * 2
    operacion3 = 9
    operación2 = operación2 * operacion3
    operación2 = "El resultado es --> " + str(operación2)
    print(operación2)

cálculo1()
#Las funciones engloban cuentas en general sin mostrar el resultado hasta que se las llame poniendo el nombre() 
#por eso siempre van primero



#función que recibe parámetros:
def cálculo2(mensaje, numero1, numero2):
    resultado = numero1 + numero2
    print(mensaje + str(resultado))

cálculo2("La suma de todo es --> ",35,70)

#función que recibe y devuelve parámetros:
def cálculo3(numero1, numero2):
    resultado = numero1 + numero2
    return resultado 
    
print(cálculo3(35,80))
print(cálculo3(35,8))
print(cálculo3(5,80))
print(cálculo3(12,20))


