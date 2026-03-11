from abc import ABC, abstractmethod

from lambdafunction import lambda_function

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        print(f"Processing the payment of {amount}")
    
    def payment_status(self):
        print("Payment Processing......")


class CreditCardPayment(Payment):
    
    def pay(self,amount):
        super().payment_status()
        print(f"{amount} is paid using Credit card")

class UPIPayment(Payment):
    def pay(self,amount):
        super().payment_status()
        print(f"{amount} is paid using UPI")        


class CashPayment(Payment):
    def pay(self,amount):
        super().payment_status()
        print(f"{amount} is paid using Cash") 


def process_payment(payment, amount):
    payment.pay(amount)

process_payment(CreditCardPayment(), 500)
process_payment(UPIPayment(), 300)
process_payment(CashPayment(), 200)


from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        print("Different vehicles use different fuels.")

class Car(Vehicle):
    def start_engine(self):
        super().fuel_type()
        print("Car engine starts with key")

class Bike(Vehicle):
    def start_engine(self):
        
        super().fuel_type()
        print("Bike starts with kick or button")


def method_type(method):
    method.start_engine()

method_type(Car())
method_type(Bike())




from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def s(self):
        pass

class Circle(Shape):
    def s(self):
        print("this is circle")

class Rectangle(Shape):
    def s(self):
        print("this is rectangle")


def shapes(method):
    method.s()

shapes(Circle())
shapes(Rectangle())
print(isinstance(shapes, Circle))  # True
print(issubclass(Rectangle, Shape)) 



from abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    @property
    def check_balance(self):
        return self.__balance

    def update_balance(self,amount):
        self.__balance+=amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def statement(self):
        return f"Account owner {self.owner} | Balance is ${self.check_balance}"


class SavingsAccount(BankAccount):
    def deposit(self,amount):
        if amount>0:
            self.update_balance(amount)
            return f"Deposited amount is {amount} | new balance: ${self.check_balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount>self.check_balance:
            return "insufficient funds"

        if amount<=0:
            return "invalid amount"

        else:
            self.update_balance(-amount)    
            return f"Withdrawn amount is ${amount} | new balance: ${self.check_balance}" 


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT=500
    def deposit(self,amount):
        if amount>0:
            self.update_balance(amount)
            return f"Deposited amount is {amount} | new balance: ${self.check_balance}"
        return  "Invalid deposit amount"

    def withdraw(self, amount):
        if amount>self.check_balance+self.OVERDRAFT_LIMIT:
            return "Overdraft amt is exceeded!!"
        self.update_balance(-amount)
        return f"Withdrawn amount is ${amount} | new balance: ${self.check_balance}" 


savings=SavingsAccount("harshil",8000)
current=CurrentAccount("nirali",7000)

print(savings.deposit(2000))
print(savings.withdraw(5000))
print(savings.statement())
print(current.deposit(100))
print(current.withdraw(6000))
print(current.statement())


"""lambda_function = lambda x,y:x+y
print(lambda_function(5,7))

def lamb_dunc(x,y):
    return x+y

print(lamb_dunc(5,7))


def abc(*args):
    return sum(args)

print (abc(1,2,3,4,5,6,6))

def example(**kwargs):
    print(kwargs)

example(name="harshil",age=23,city="vadodara")"""