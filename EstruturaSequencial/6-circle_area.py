# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio: "))

def calcula_area(area):
    pi = math.pi
    raio2 = math.pow(raio,2)
    area = pi * raio2
    return round(area,2)

print(calcula_area(raio))