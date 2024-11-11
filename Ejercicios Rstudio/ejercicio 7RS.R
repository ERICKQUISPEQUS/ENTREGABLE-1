valores <- rnorm(1000, mean = 75, sd = 20)

hist(valores, main = "Histograma de la muestra", xlab = "Valores", col = "lightblue", border = "black")

media_muestra <- mean(valores)
cat("La media de la muestra es:", media_muestra, "\n")
