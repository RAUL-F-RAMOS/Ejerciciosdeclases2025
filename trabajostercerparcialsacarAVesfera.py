#Sacar el area y volumen de una esfera


import math

def calcular_area_volumen_esfera(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo.")
    
    area = 4 * math.pi * radio**2
    volumen = (4/3) * math.pi * radio**3
    
    return area, volumen

try:
    radio = float(input("Ingrese el radio de la esfera: "))
    area, volumen = calcular_area_volumen_esfera(radio)
    print(f"Área de la esfera: {area:.2f}")
    print(f"Volumen de la esfera: {volumen:.2f}")
except ValueError as e:
    print(f"Error: {e}")