import pandas as pd
#
df=pd.read_csv("highscores.csv",header=0)
print(df)
print(df['first_name'])
print(df['integer'])
#
high=df['integer'].max()
low=df['integer'].min()
ave=df['integer'].mean()
total=df['integer'].sum()
med=df['integer'].median()
mode=df['integer'].mode()
print(high,low,ave,total,med,mode)
#
hscorer=df.loc[df['integer']==high,'first_name'].iloc[0]
lscorer=df.loc[df['integer']==low,'first_name']
print(hscorer,lscorer)
#
sortedDF=df.sort_values(by='integer')
sortedDF.to_csv('highscores-sorted.csv',index=False)
    
