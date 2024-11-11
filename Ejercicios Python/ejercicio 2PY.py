import numpy as np

# Generar una muestra de 300 valores con media=60 y desviación estándar=12
muestra = np.random.normal(loc=60, scale=12, size=300)

# Calcular el percentil 90
percentil_90 = np.percentile(muestra, 90)

# Mostrar el resultado
print(f"Percentil 90: {percentil_90}")
