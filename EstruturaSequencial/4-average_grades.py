# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

for i in range(4):
    grade = int(input("Digite a nota do %d° bimestre: " % (i+1)))
    media =+ grade

print("A média é %d" % media)