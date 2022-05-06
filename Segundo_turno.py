#Estamos em ano de eleição e por isso o Tribunal Superior Eleitoral nos procurou para que fizéssemos um programa para um possível segundo turno, a mensagem que recebemos foi a seguinte: 
#“Considerando uma eleição de apenas 2 candidatos, faça um programa que leia do teclado o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato.
#Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos”

print ("\t----------------------")
print ("\t| Máquina de eleição |")

num_total_eleitores = int(input("   Insira o numero total de eleitores: "))
cand1 = int(input("   Insira o numero de votos do candidato 1: "))
cand2 = int(input("   Insira o numero de votos do candidato 2: "))
porc1 = (cand1/num_total_eleitores)*100
porc2 = (cand2/num_total_eleitores)*100

print ("   Candidato 1: ",porc1,"% / Candidato 2: ",porc2,"%")
print ("\t----------------------")
