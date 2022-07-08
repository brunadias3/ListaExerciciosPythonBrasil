# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

salario = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalha no mês? "))
salario_total = horas*salario
print("Salario total é R$ %.2f" % salario_total)