from logging import PercentStyle

#A Loja Limão com Mel está vendendo seus produtos em 7 (sete) prestações sem juros. 
# Faça um programa que receba um valor de uma compra e mostre o valor das prestações


print ("\t--------------------------")
print ("\t| Máquina de prestrações |")

compra = float(input("     Insira o valor da compra : "))
prest = float(input("     Insira a quantidade de prestações : "))
val = compra/prest

print ("     O valor a pagar em cada prestação é :",val,"Reais")
print ("\t-------------------------")
