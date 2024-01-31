km= int(input('Quantos km o carro percorreu ?'))
day= int(input('Quantos dias alugados ?'))
pagar = (km*0.15) + (day*60)
print(f'Total a ser pago : R${pagar:.2f}')