c=float(input('Dígite o valor da sua carteira em reais :'))
d=(c/3.27)
s=(c % 3.27)
print(f'Você pode comprar US${d:.2f}  com os seus R${c:.2f} e sobra {s:.2f} reias')
