velocidade_maxima = 80
velocidade = int(input("Digite o valor da velocidade : "))
if velocidade > velocidade_maxima and velocidade <= 90:
    print(" Você pegou uma multa leve ")
elif velocidade > velocidade_maxima and velocidade <=100 :
    print("Você pegou uma multa grave ")
elif velocidade > velocidade_maxima and velocidade > 100:
    print("Você pegou uma multa gravíssima") 
else:
    velocidade==velocidade_maxima
    print("Você não sofreu nenhuma multa ")