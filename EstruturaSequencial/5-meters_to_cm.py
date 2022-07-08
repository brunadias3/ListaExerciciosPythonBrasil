# Faça um Programa que converta metros para centímetros.

def meters_to_cm(meters):
    cm = meters * 100
    return cm

metro = int(input("Metros: "))
print("Centímetros: %d" % meters_to_cm(metro))