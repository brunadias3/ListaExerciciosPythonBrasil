# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcula_area(quadrado):
    area = quadrado * quadrado
    return area

def double_area(area):
    double = calcula_area(quadrado) * 2
    return double

quadrado = int(input("Medida: "))
print("Area: ", calcula_area(quadrado))
print("Dobro: ", double_area(quadrado))