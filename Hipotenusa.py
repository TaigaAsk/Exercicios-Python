import math

print ("\t-------------------------")
print ("\t| Máquina de hipotenusa |")

cat1 = float(input("     Insira o valor do cateto 1 : "))
cat2 = float(input("     Insira o valor do cateto 2 : "))
hip = math.sqrt((cat1**2)+(cat2**2))

print ("     O valor da hipotenusa é :",hip)
print ("\t-------------------------")
