import numpy as np

# Generar una muestra de 500 valores de una normal estándar (media=0, desviación estándar=1)
muestra = np.random.normal(loc=0, scale=1, size=500)

# Contar cuántos valores están entre -1 y 1
valores_entre_minus_1_y_1 = np.sum((muestra >= -1) & (muestra <= 1))

# Calcular el porcentaje
porcentaje = (valores_entre_minus_1_y_1 / len(muestra)) * 100

# Mostrar el resultado
print(f"Porcentaje de valores entre -1 y 1: {porcentaje:.2f}%")
