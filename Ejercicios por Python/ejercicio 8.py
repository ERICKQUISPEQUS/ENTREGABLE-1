import scipy.stats as stats

# Parámetros de la distribución
mu = 75  # media
sigma = 8  # desviación estándar
x1 = 70  # puntaje inferior
x2 = 85  # puntaje superior

# Calcular los valores Z
z1 = (x1 - mu) / sigma
z2 = (x2 - mu) / sigma

# Calcular las probabilidades acumuladas para cada Z
probabilidad = stats.norm.cdf(z2) - stats.norm.cdf(z1)

print(f"La probabilidad de que un estudiante obtenga un puntaje entre 70 y 85 es {probabilidad:.4f}")
