import scipy.stats as stats

# Parámetros de la distribución
mu = 25  # media
sigma = 4  # desviación estándar
x = 20  # valor que queremos evaluar

# Calcular el valor Z
z = (x - mu) / sigma

# Calcular la probabilidad de que la orden se procese en menos de 20 minutos
probabilidad = stats.norm.cdf(z)

print(f"La probabilidad de que una orden se procese en menos de 20 minutos es {probabilidad:.4f}")
