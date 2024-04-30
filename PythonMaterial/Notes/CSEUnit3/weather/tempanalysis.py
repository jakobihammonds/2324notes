import pandas as pd
import math
file= pd.read_csv("TempData.csv",header=0)

#print(file["TMAX"])
#print(file["TMIN"])

file["TMIN"]=file["TMIN"].replace(-9999,math.nan)
#file.dropna(subset=["TMIN"],inplace=True)

file["TMAX"]=file["TMAX"].replace(-9999,math.nan)
#file.dropna(subset=["TMAX"],inplace=True)

gap =[]

try:
  for i in range(len(file)):
   diff = file["TMAX"][i]-file["TMIN"][i]
   gap.append(diff)
except:
 print(file[i])

bigdif = (max(gap))

locationOfBigDif = gap.index(bigdif)
print(f'''
the largest gap between the min and max was on {file["DATE"][locationOfBigDif]},
the temp diff was {max(gap)}
'''
)