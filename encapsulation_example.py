class bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def updatebalance(self,balance):
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited amount is {amount} and new balance is {self.__balance}")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficent funds")
        else:
            self.__balance-=amount
            print(f"amount withdrawn is {amount} and new balance is {self.__balance}")

    def getbalance(self):
        return self.__balance
    

acc=bankaccount("harshil", 5000)
acc.deposit(500)
acc.withdraw(2500)
print(acc.getbalance())