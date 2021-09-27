df=read.csv("data.csv",header=T, row.names=1, dec = ",",sep=";")

str(df)
h=hclust(dist(df))
plot(h, main="Clustering")



