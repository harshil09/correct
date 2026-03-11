import pandas as pd

df=pd.read_csv("C:/Users/harsh/OneDrive/Desktop/db.csv")
print(df)

accnumber=int(input("Enter account number="))
pin=int(input("Enter account pin="))

user=df[(df["acc_num"] == accnumber) & (df["acc_pin"]==pin)]

if not user.empty:
    balance=user.iloc[0]["initial_balance"]
    print(balance)
    print("Login successful")
else:
    print("invalid acc number and pin")