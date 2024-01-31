import random 
numero_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
 numero_digitado = int(input( "Digite um número : "))
 if numero_digitado > numero_aleatorio:
    print("Numero errado, chute um valor menor")
 elif numero_digitado < numero_aleatorio:
    print("Numero errado, chute um valor maior")
 elif  numero_digitado == numero_aleatorio:
    acertou = True
    print("Parabéns !! Você acertou.")

1