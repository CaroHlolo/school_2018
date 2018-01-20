import numpy as np
import matplotlib.pyplot as pl

data1=np.loadtxt("testdata.csv",delimiter=",",skiprows=1)
#pl.figure(1)
pl.plot(data1[:,0],data1[:,1],"r--*")
#pl.show()

pl.xlabel("time")
pl.ylabel("${}^0C$")
pl.subplot(1,2,1) #

xx=np.arange(0,100,.5)
yy=np.sin(xx/100*np.pi)*20+10
pl.legend(["temp","sine"])

pl.plot(xx,yy,"b")
#pl.show()
#pl.title("temp vs time")
#pl.legend(["temp", "sine"])
pl.xlim(xmax=150,xmin=0)
pl.title("graph")
#pl.show()

#pl.figure(2)

pl.subplot(1,2,2)
pl.plot(data1[:,0],data1[:,3],"y.-")
pl.show()

