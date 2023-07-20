Auto = read.csv("Auto.csv", header=T, na.strings="?")
Auto = na.omit(Auto)

# (a)
pairs(Auto)

# (b)
# cor(Auto[,1:7])

# (c)
# attach(Auto)