# Coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
#Listas
precos = [20,50,200]
#         0 , 1 , 2
print(precos[0])
print(precos.index(200))
print(precos[2])
#Listas

diversidades = [15, 'jhonathan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

#Laços em interáveis

for preco in precos:
    print(preco)

for diversidade in diversidades:
    print(diversidade)


'''Some os valores dados uma coleção de dados ''idades'' [15,46,75,34,23]
,imprima na tela a soma desses valores
'''
idades=[15,46,75,34,23]
total = 0
for idade in idades:
    total = total +idade
    print(total)


