#################################################################################################################
####### Стандартна кластеризація
df=read.csv("kam3.csv",header=T, row.names=1, dec = ",",sep=";")



str(df)
dummy_df=data.frame(rep(0,42))
library(dummies)
for (i in 5:length(df))
dummy_df=cbind(dummy_df,dummy(df[,i]))


row.names(dummy_df)=row.names(df)
h=hclust(dist(dummy_df[,-1]))
plot(h,main="1 модель(звичайна метрика)")



####### Зображення на площині
h2=hcut(dummy_df[,-1],4)
clus=as.integer(h2$cluster)


library(ggplot2)
tmp=data.frame(df$Скільки.ЗА,df$Скільки.був.присутнім, clus)
names(tmp)=c("za","prys","cluster")
ggplot(data=tmp,aes(za,prys))+geom_point(size=4,col=tmp$cluster)




#################################################################################################################
####### Моя метрика - порівняння голосувань по присутності

df=read.csv("kam4.csv",header=T, row.names=1, dec = ",",sep=";")
my_dist<-function(df1)
{
  n=length(df1[,1])
  d=matrix(NA,nrow=n,ncol=n)
  for(i in 1:n)
  {
    for(j in 1:i)
    {
       d[i,j]=sum(df1[i,]!=df1[j,],na.rm=T)
       d[j,i]=d[i,j]
    }
  }
  dimnames(d)=list(row.names(df1),row.names(df1))
  return(d)
}

d=my_dist(df[,c(5:length(df))])
plot(hclust(as.dist(d)),main="2 модель(відмінність між голосами)")



################################################################################################################
####### Побудова опозиційної моделі

####### МОдель 1 (по всім данним)

library(ggplot2)
df=read.csv("opoz.csv",header=T, row.names=1, dec = ",",sep=";")
str(df)
kand=df[-48,-1]
result=as.vector(df[48,-1])
coef=rep(0,47)
for(i in 1:47)
{
  coef[i]=(sum(result==1&kand[i,]==1)+sum(result==0&kand[i,]!=1))/159
}
y=rep(1,47)
tmp_df=data.frame(coef,y,df[-48,1],row.names = row.names(kand))

ggplot(aes(x=coef,y=y),data=tmp_df)+geom_point()+xlim(0.4,0.85)+ylim(0,2)+geom_label_repel(
  aes(coef, y, fill=df..48..1., label = rownames(tmp_df)),
  color = 'white',
  box.padding = unit(0.45, "lines"),
  label.padding = unit(0.08, "lines"))


####### МОдель 2 (лише по присутності)

library(ggplot2)
df=read.csv("opoz.csv",header=T, row.names=1, dec = ",",sep=";")
str(df)
kand=df[-48,-1]
result=as.vector(df[48,-1])
coef=rep(0,47)
for(i in 1:47)
{
  coef[i]=(sum(result==1&kand[i,]==1)+sum(result==0&kand[i,]!=1&kand[i,]!=-1))/sum(kand[i,]!=-1)
}
y=rep(1,47)
tmp_df=data.frame(coef,y,df[-48,1],row.names = row.names(kand))

ggplot(aes(x=coef,y=y),data=tmp_df)+geom_point()+xlim(0.4,0.85)+ylim(0,2)+geom_label_repel(
  aes(coef, y, fill=df..48..1., label = rownames(tmp_df)),
  color = 'brown',
  box.padding = unit(0.45, "lines"),
  label.padding = unit(0.08, "lines"))


####### МОдель 3 (лише неприйняті рішення)

library(ggplot2)
df=read.csv("opoz2.csv",header=T, row.names=1, dec = ",",sep=";")
str(df)
kand=df[-48,-1]
result=as.vector(df[48,-1])
coef=rep(0,47)
for(i in 1:47)
{
  coef[i]=(sum(result==1&kand[i,]==1)+sum(result==0&kand[i,]!=1&kand[i,]!=-1))/sum(kand[i,]!=-1)
}
y=rep(1,47)
tmp_df=data.frame(coef,y,df[-48,1],row.names = row.names(kand))

ggplot(aes(x=coef,y=y),data=tmp_df)+geom_point()+xlim(0.4,0.85)+ylim(0,2)+geom_label_repel(
  aes(coef, y, fill=df..48..1., label = rownames(tmp_df)),
  color = 'white',
  box.padding = unit(0.45, "lines"),
  label.padding = unit(0.08, "lines"))
