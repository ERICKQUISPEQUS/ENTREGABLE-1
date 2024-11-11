media <- 75
desviacion_estandar <- 15

probabilidad_65_85 <- pnorm(85, mean = media, sd = desviacion_estandar) - pnorm(65, mean = media, sd = desviacion_estandar)

cat("La probabilidad de que un valor esté entre 65 y 85 es:", probabilidad_65_85, "\n")
