import pandas as pd
import math
import matplotlib.pyplot as plt
file = pd.read_csv('TempData.csv',header=0)
###   GET RID OF -9999   ###
file["TMIN"]=file["TMIN"].replace(-9999,math.nan)
file["TMAX"]=file["TMAX"].replace(-9999,math.nan)
file["TAVG"]=file["TAVG"].replace(-9999,math.nan)
###  FINDING THE MAX   ###
xdata=range(len(file))
plt.plot(xdata,file['TMAX'])
plt.plot(xdata,file['TMIN'])
plt.plot(xdata,file['TAVG'])
plt.ylabel("TMAX, TMIN, TAVG")
plt.xlabel("Date")
plt.legend(["TMAX","TMIN","TAVG"], loc="lower right")
plt.title("TMAX, TMIN, TAVG over time")
plt.show()