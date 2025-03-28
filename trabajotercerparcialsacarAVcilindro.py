#Sacar el area y volumen de un cilindro
import math

def calcular_area_cilindro(radio, altura):
 
    area = 2 * math.pi * radio * altura + 2 * math.pi * radio**2
    return area

def calcular_volumen_cilindro(radio, altura):
 
    volumen = math.pi * radio**2 * altura
    return volumen

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area = calcular_area_cilindro(radio, altura)
volumen = calcular_volumen_cilindro(radio, altura)

print(f"El área del cilindro es: {area:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")