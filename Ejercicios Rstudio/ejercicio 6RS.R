media <- 80
desviacion_estandar <- 10

probabilidad_mayor_90 <- 1 - pnorm(90, mean = media, sd = desviacion_estandar)

cat("La probabilidad de obtener un valor mayor a 90 es:", probabilidad_mayor_90, "\n")
