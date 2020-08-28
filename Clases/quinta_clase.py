#--------Preguntas------#
preguntaNumero = 'ingrese un número del 1 al 10 : '
#--------Mensajes-------#
mensajeFallido = 'Fallaste!!, no es el número secreto'
mensajeExitoso = 'Felicitaciones has acertado el número en el que pensé'
mensajeDerrota = 'Lo siento has perdido'
mensajeDespedida = 'Gracias por jugar nos vemos'
mensajeVida= 'Ten cuidado has perdido {} vida te quedan {}'
#Ciclos while

numeroSecreto = 6
numeroIngresado = int(input(preguntaNumero))
vidasPerdidas=0
while(numeroSecreto != numeroIngresado and vidasPerdidas<=2):
    vidasPerdidas =vidasPerdidas +1 
    print(mensajeVida.format(vidasPerdidas,3-vidasPerdidas))
    print(mensajeFallido)
    if vidasPerdidas <3:
        numeroIngresado = int(input(preguntaNumero))

if vidasPerdidas <3:
    print(mensajeExitoso)
else: 
    print(mensajeDerrota)
print(mensajeDespedida)


