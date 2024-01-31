v=float(input('Digite o valor abaixo em metros para a conversão :'))
km=v/1000
hm=v/100
dam=v/10
dm=v*10
cm=v*100
mm=v*1000
type(print(f'o seu valor {v}m corresponde a : \n{km:}km \n{hm}hm \n{dam}dam', end=
            f'\n{dm}dm \n{cm:.0f}cm \n{mm:.0f}mm'))