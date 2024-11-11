import scipy.stats as stats

# Parámetros de la distribución
mu = 1200  # media
sigma = 100  # desviación estándar
x = 1300  # valor que queremos evaluar

# Calcular el valor Z
z = (x - mu) / sigma

# Calcular la probabilidad de que la bombilla dure más de 1300 horas
probabilidad = 1 - stats.norm.cdf(z)

print(f"La probabilidad de que una bombilla dure más de 1300 horas es {probabilidad:.4f}")
