
##set the correct folder as enviroment
setwd("C:/Users/longa/Desktop/SPE/seconodoAsignment/Spe_second_assignment/spe-py-nwsim")

par(mfrow=c(1,3))
dat = read.csv("temp.csv", header = TRUE)
tr1=dat[dat$dst==1,]$tr
tr2=dat[dat$dst==2,]$tr
tr3=dat[dat$dst==3,]$tr
tr4=dat[dat$dst==4,]$tr
tr5=dat[dat$dst==5,]$tr
tr6=dat[dat$dst==6,]$tr
tr7=dat[dat$dst==7,]$tr
tr8=dat[dat$dst==8,]$tr
tr9=dat[dat$dst==9,]$tr
tr10=dat[dat$dst==10,]$tr

plot(tr1,ylim=c(0,2.3),type='l',main="dieci nodi")
lines(tr2,col="red")
lines(tr3,col="green")
lines(tr4,col="blue")
lines(tr5,col="yellow")
lines(tr6,col="orange")
lines(tr7,col="brown")
lines(tr8,col="violet")
lines(tr9,col="purple")
lines(tr10,col="pink")




cr1=dat[dat$dst==1,]$cr
cr2=dat[dat$dst==2,]$cr
cr3=dat[dat$dst==3,]$cr
cr4=dat[dat$dst==4,]$cr
cr5=dat[dat$dst==5,]$cr
cr6=dat[dat$dst==6,]$cr
cr7=dat[dat$dst==7,]$cr
cr8=dat[dat$dst==8,]$cr
cr9=dat[dat$dst==9,]$cr
cr10=dat[dat$dst==10,]$cr

plot(cr1,type="l")
lines(cr2,col="red")
lines(cr3,col="green")
lines(cr4,col="blue")
lines(cr5,col="yellow")
lines(cr6,col="orange")
lines(cr7,col="brown")
lines(cr8,col="violet")
lines(cr9,col="purple")
lines(cr10,col="pink")
legend("bottomright", legend=c("n1","n2","n3","n4","n5","n6","n7","n8","n9","n10"),
       col=c("black","red", "green","blue","yellow","orange","brown","violet","purple","pink"), lty=1
       , cex=0.6,bty = "n")

dr1=dat[dat$dst==1,]$dr
dr2=dat[dat$dst==2,]$dr
dr3=dat[dat$dst==3,]$dr
dr4=dat[dat$dst==4,]$dr
dr5=dat[dat$dst==5,]$dr
dr6=dat[dat$dst==6,]$dr
dr7=dat[dat$dst==7,]$dr
dr8=dat[dat$dst==8,]$dr
dr9=dat[dat$dst==9,]$dr
dr10=dat[dat$dst==10,]$dr

plot(dr1,type="l")
lines(dr2,col="red")
lines(dr3,col="green")
lines(dr4,col="blue")
lines(dr5,col="yellow")
lines(dr6,col="orange")
lines(dr7,col="brown")
lines(dr8,col="violet")
lines(dr9,col="purple")
lines(dr10,col="pink")

