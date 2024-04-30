import pandas as pd
import matplotlib.pyplot as plt
import math as m
# ^ imports
file=pd.read_csv("temperature_data.csv",header=0)
#clean data

#analyze data

#visualize data
plt.plot(file['Year'],file['Anomaly'])
plt.ylabel("Temp Anomalies")
plt.xlabel("Year")
plt.title("Temp Anomalies Over Time")
plt.show()
