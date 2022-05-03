# Tirulipa irá fazer uma turnê internacional e ele quer fazer uma estimativa de quantos ingressos ele precisa vender para cobrir o custo de cada show e quantos ingressos ele precisa vender para ter lucro em cada apresentação.
# Vamos usar nossos conhecimentos para ajudar tirulipa, fazendo um programa que receba o custo de um show e o preço do ingresso, calcule e mostre: 
# A quantidade de ingressos que devem ser vendidos para que pelo menos o custo do show seja alcançado.
# A quantidade de ingressos que devem ser vendidos para que se tenha um lucro de 23%.

print ("\t------------------------")
print ("\t|   Show do tirulipa   |")

custo = float(input("     Insira o custo do show: "))
ingresso = float(input("     Insira o preço do ingresso: "))

show = custo / ingresso
lucro = (custo*0.23) + custo / ingresso

print (" A quantidade de ingressos que devem ser vendidos para que atinja o custo do show: ", show)
print (" A quantidade de ingressos que devem ser vendidos para que se tenha um lucro de 23 por cento: ", lucro)

print ("\t------------------------")
