import glob
import numpy as np
import math as mt


alist = glob.glob("*day.csv")
mon=np.loadtxt("monday.csv",delimiter=",",skiprows=1,usecols=[1,2,3,4,]) #this reads from textfile
tues=np.loadtxt("tuesday.csv",delimiter=",",skiprows=1,usecols=[1,2,3,4,])
wed=np.loadtxt("wednesday.csv",delimiter=",",skiprows=1,usecols=[1,2,3,4,])


#for i in range (len(alist)):
	
mon_max=[np.max(mon[:,0])]
tues_max=[np.max(tues[:,0])]
wed_max=[np.max(wed[:,0])]


#print("max for monday: ", str(mon_max))
#print(tues_max)
#print(wed_max)

array_list= [mon_max,tues_max,wed_max]

np.savetxt("max_list",array_list,delimiter=",") #this add to text file





