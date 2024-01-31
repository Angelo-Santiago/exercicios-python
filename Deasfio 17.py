import math
co=float(int(input("Digite o comprimento do cateto oposto :")))
ca=float(int(input("Digite o comprimento do cateto adjacente :")))
hi= (co**2) + (ca**2)
rhi= math.sqrt(hi)
print(f"O comprimento da hipotenusa do seu triângulo retangulo é igual à : {rhi:.2f}")
