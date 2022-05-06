#Faça um programa que receba o peso e a altura de uma pessoa e calcule o índice de massa corpórea. Ele mede a relação entre peso e altura 
# (peso em Kg, dividido pelo quadrado da altura em metros).

print ("\t------------------")
print ("\t| Máquina de IMC |")

peso = float(input("     Insira o peso (em quilos) : "))
altura = float(input("     Insira a altura (em metros) : "))
imc = peso/(altura**2)

print ("     O indice de massa corporea é: ", imc)
print ("\t------------------")