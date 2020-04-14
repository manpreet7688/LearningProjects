'''For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.'''

class BankAccount():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Hi! {}, The balance in your account is {}".format(self.owner, self.balance)

    def deposit(self, money):
        self.balance = self.balance + money
        print("Deposite Accepted")
        print("The amount is now {}".format(self.balance))

    def withdraw(self,money_amt):
        if self.balance >= money_amt:
            self.balance = self.balance - money_amt
            print("Withdrawal Successful")
        else:
            print("Funds unavailable")






bank_detail = BankAccount("Jose", 100)
print(bank_detail)
print(bank_detail.owner)
print(bank_detail.balance)

bank_detail.deposit(50)
bank_detail.withdraw(75)
bank_detail.withdraw(500)
