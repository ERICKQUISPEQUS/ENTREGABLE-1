import numpy as np

# Generar una muestra de 750 valores con media=55 y desviación estándar=5
muestra = np.random.normal(loc=55, scale=5, size=750)

# Calcular la media y la desviación estándar
media = np.mean(muestra)
desviacion_estandar = np.std(muestra)

# Mostrar los resultados
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")
