nublado = True
aburrido = False
aburrido = not (aburrido) #el aburrido false se transforma en true x doble negación 


if nublado== True:
    print("Está nublado")
    if aburrido== True:
        print("ya que está nublado y estamos aburridos vamos al cine")

#versión abreviada  (los dos tienen q estar igual):
if nublado == True and aburrido == True:
    print("ya que está nublado y estamos aburridos vamos al cine")

#solamente uno necesita ser cierto no importa si es true or false:
if nublado == True or aburrido == True:
    print("ya que está nublado y estamos aburridos vamos al cine")