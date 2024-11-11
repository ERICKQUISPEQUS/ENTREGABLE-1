muestra <- rnorm(250, mean = 50, sd = 7)

prueba_normalidad <- shapiro.test(muestra)

cat("Resultados de la prueba de normalidad de Shapiro-Wilk:\n")
print(prueba_normalidad)
