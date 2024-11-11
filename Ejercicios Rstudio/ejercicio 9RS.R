observaciones <- rnorm(500, mean = 40, sd = 10)

percentil_75 <- quantile(observaciones, 0.75)

cat("El percentil 75 es:", percentil_75, "\n")
