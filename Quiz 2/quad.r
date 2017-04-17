
sum <- 0

for (i in 1:100) {
	coeffs <- sample(-20:20,3,replace=T)
	names(coeffs) <- c("a","b","c")
	x <- seq(-3,3,length=200)
	y <- coeffs[1]*x^2+coeffs[2]*x+coeffs[3]
	plot(x,y)
	disc <- coeffs[2]^2-4*coeffs[1]*coeffs[3]

	if (disc > 0) {
		sum <- sum + 1
	}
}
