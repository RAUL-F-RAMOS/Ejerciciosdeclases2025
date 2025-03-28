#sacar el area y volumen de un cono truncado

import math

def calcular_area_y_altura_cono_truncado(r1, r2, h):


    generatriz = math.sqrt((r1 - r2)**2 + h**2)
    area_lateral = math.pi * generatriz * (r1 + r2)
    area_base_mayor = math.pi * r1**2
    area_base_menor = math.pi * r2**2
    area_total = area_lateral + area_base_mayor + area_base_menor
    
    return {
        "area_lateral": area_lateral,
        "area_total": area_total,
        "altura": h
    }

if __name__ == "__main__":
    radio_mayor = float(input("Ingrese el radio mayor (r1): "))
    radio_menor = float(input("Ingrese el radio menor (r2): "))
    altura = float(input("Ingrese la altura (h): "))
    
    resultados = calcular_area_y_altura_cono_truncado(radio_mayor, radio_menor, altura)
    
    print(f"Área lateral: {resultados['area_lateral']:.2f}")
    print(f"Área total: {resultados['area_total']:.2f}")
    print(f"Altura: {resultados['altura']:.2f}")