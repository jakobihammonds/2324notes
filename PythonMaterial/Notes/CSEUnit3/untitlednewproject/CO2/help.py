import pandas as pd
import matplotlib.pyplot as plt
import math as m
# ^ imports
file=pd.read_csv("co2_data.csv",header=5)
#clean data
file['Average'] = file['Average'].replace(-99.99,m.nan)
#function below drops all NaN's from the list
file.dropna(subset=['Average'],inplace=True)
#analyze data

#visualize data
plt.plot(file['decimal_year'],file['Average'])
plt.ylabel("Avg CO2")
plt.xlabel("Years")
plt.title("Average CO2 Over Time")
plt.show()
