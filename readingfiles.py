import pandas as pd

df=pd.read_csv("C:/Users/harsh/Downloads/customers-100.csv", usecols=["Index", "First Name"])
print(df.head())

#used when we want to automatically call 5 columns with knowing name 
# :->all rownas and :5 first 5 columns
#df1=df.iloc[:, :5]
#print(df1)