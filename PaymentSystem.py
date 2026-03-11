from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def getbalance(self):
        pass

class UPIPayment(Payment):
    def __init__(self,id,balance):
        self.id=id
        self.__balance=balance #encapsulation

    #property
    @property
    def balance(self):
        return self.__balance

    #setter with validation
    @balance.setter
    def balance(self,value):
        if value>=0:
            self.__balance=value
        else:
            raise ValueError ("Invalid transaction")

    def pay(self,amount):
        if amount>self.__balance:
            raise ValueError ("Insufficient funds")
        self.__balance-=amount
        print(f"UPI Payment of {amount} is successful")


    def getbalance(self):
        return f"New balance is {self.balance}"
 
class CardPayment(Payment):

    def __init__(self,balance):
        self.__balance=balance

    def pay(self,amount):
        fee=amount*0.05
        total=amount+fee

        if total>self.__balance:
            raise ValueError ("Insufficient funds")

        self.__balance-=amount
        print(f"card payment of {amount} and applicable fess was {fee} was successful")

    def getbalance(self):
        return f"New balance is {self.balance}"

c=UPIPayment(1,9500)
print(c.pay(800))
print(c.getbalance)
d=CardPayment(10000)
print(d.pay(900))
print(c.getbalance)
