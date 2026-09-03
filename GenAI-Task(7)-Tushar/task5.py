# Task 5 - Abstraction (Using Abstract Base Class)

# Import ABC, abstractmethod
from abc import ABC, abstractmethod

# Create an abstract Payment class with abstract method
class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass

# Create a CreditCardPayment subclass with override process_payment()
class CreditCardPayment(Payment):

    # Initialize the Constructor
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"The amount of {self.amount} rs proceed by Credit Card Payment"
    
# Create a UPIPayment subclass with override process_payment()
class UPIPayment(Payment):

    # Initialize the Constructor
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"The amount of {self.amount} Rs proceed by UPI Payment"

# Create 2 objects CreditCard and UPI Payment
credit_card = CreditCardPayment(10000)
upi = UPIPayment(4000)

# Show both result
print(credit_card.process_payment())
print(upi.process_payment())




