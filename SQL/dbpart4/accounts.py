import pandas as pd
file = pd.read_csv("Accounts.csv", header=0)

queries=""
for i in range(len(file)):
     try:
      queryString = f"INSERT INTO Accounts (Name,Address,City,State,Zip,Phone) VALUES ('{file['name'][i]}')
      ('{file['address'][i]}')
      ('{file['city'][i]}')
      ('{file['state'][i]}')
      ('{file['zip'][i]}')
      ('{file['phone'][i]}');"
      queries+=queryString+"\n"
     except:
      print(i)
     
with open("AccountsUpload.sql","w+") as file:
     file.write(queries)