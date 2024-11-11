import scipy.stats as stats

# Parámetros de la distribución
mu = 50  # media
sigma = 5  # desviación estándar
x = 45  # valor que queremos evaluar

# Calcular el valor Z
z = (x - mu) / sigma

# Calcular la probabilidad de que la pieza pese menos de 45 gramos
probabilidad = stats.norm.cdf(z)

print(f"La probabilidad de que la pieza pese menos de 45 gramos es {probabilidad:.4f}")
