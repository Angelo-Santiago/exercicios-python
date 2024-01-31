p = float(input("Insira o preço do produto para obter o desconto:"))
d = p * 5/100
vf= p - d
print(f'O valor do seu produtor de R${p:.2f} com o desconto de R${d:.3f} ficará'
      f' por R${vf:.3f}')