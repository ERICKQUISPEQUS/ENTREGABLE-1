import numpy as np
import scipy.stats as stats

# Generar una muestra de 400 valores con media=100 y desviación estándar=15
muestra = np.random.normal(loc=100, scale=15, size=400)

# Calcular la media y la desviación estándar de la muestra
media_muestra = np.mean(muestra)
desviacion_estandar_muestra = np.std(muestra, ddof=1)  # ddof=1 para muestra, no población

# Calcular el error estándar
error_estandar = desviacion_estandar_muestra / np.sqrt(len(muestra))

# Determinar el valor crítico z para un intervalo de confianza del 90%
z_90 = stats.norm.ppf(0.95)  # 0.95 para el 90% de intervalo

# Calcular el intervalo de confianza
margen_error = z_90 * error_estandar
intervalo_confianza = (media_muestra - margen_error, media_muestra + margen_error)

# Mostrar el resultado
print(f"Intervalo de confianza al 90% para la media: {intervalo_confianza}")
