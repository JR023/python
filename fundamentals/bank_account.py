class BankAccount:
    # don't forget to add some default values for these parameters!
    int_rate=.01
    balance=0
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate= int_rate
        self.account_balance= balance
    def deposit(self, amount):
        # your code here
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount > self.account_balance:
            print ("Insufficent Funds: Charging a $5 fee")
            self.account_balance = self.account_balance- 5
        else:
            self.account_balance -= amount
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.account_balance}")
        return self
    def yield_interest(self):
        # your code here
        self.account_balance = self.account_balance * (1+self.int_rate)
        return self
#instances
account1 = BankAccount (.10, 2500) 
account2 = BankAccount(.10,2000) 
#display info
account1.display_account_info()
account1.deposit(200).deposit(100).deposit(200).withdraw(3600).yield_interest().display_account_info()
account2.display_account_info()
account2.deposit(300).deposit(800).withdraw(200).withdraw(100).withdraw(400).withdraw(500).yield_interest().display_account_info()

