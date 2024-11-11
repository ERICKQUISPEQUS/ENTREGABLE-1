import numpy as np
import matplotlib.pyplot as plt

# Generar dos distribuciones normales
muestra_1 = np.random.normal(loc=45, scale=5, size=500)
muestra_2 = np.random.normal(loc=60, scale=10, size=500)

# Calcular las medias
media_1 = np.mean(muestra_1)
media_2 = np.mean(muestra_2)

# Mostrar las medias
print(f"Media de la primera muestra: {media_1}")
print(f"Media de la segunda muestra: {media_2}")

# Graficar los histogramas
plt.figure(figsize=(10, 6))
plt.hist(muestra_1, bins=30, alpha=0.5, label='Muestra 1 (media=45, desv=5)', color='black')
plt.hist(muestra_2, bins=30, alpha=0.5, label='Muestra 2 (media=60, desv=10)', color='orange')

# Añadir detalles a la gráfica
plt.title('Comparación de los histogramas de dos distribuciones normales')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()

# Mostrar la gráfica
plt.show()
