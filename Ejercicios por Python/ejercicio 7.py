import scipy.stats as stats

# Parámetros de la distribución
mu = 170  # media
sigma = 10  # desviación estándar
x = 180  # valor que queremos evaluar

# Calcular el valor Z
z = (x - mu) / sigma

# Calcular la probabilidad de que el estudiante mida más de 180 cm
probabilidad = 1 - stats.norm.cdf(z)

print(f"La probabilidad de que un estudiante mida más de 180 cm es {probabilidad:.4f}")
