# A cidade de PETlândia está passando por um período de crise, então os comerciantes estão tentando oferecer descontos para não perder os clientes. 
# Um desses comerciantes está pedindo sua ajuda, ele precisa que você faça um algoritmo que receba um valor da compra total do cliente e aplique um desconto de 7% sobre o preço, depois imprima na tela o resultado.

print ("\t-----------------------")
print ("\t| Máquina de desconto |")

valtotal = float(input("     Insira o valor total da compra : "))
desc = float(input("     Insira o desconto que será aplicado : "))
valor = (valtotal-((desc/100)*valtotal))

print ("     O valor com desconto será :",valor,"Reais")
print ("\t-----------------------")