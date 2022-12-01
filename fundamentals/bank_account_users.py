class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount, account_name):
        # your code here
        self.account_balance += amount
        return self

    def withdraw(self, amount, account_name):
        # your code here
        if amount > self.account_balance:
            print ("Insufficent Funds: Charging a $5 fee")
            self.account_balance = self.account_balance- 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        # your code here
        return f"{self.balance}"

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User: 
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.03,4000),
            "savings" : BankAccount(.07,2000)
        }
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
#instances
jordan = User ("Jordan")

#display info
jordan.account['checking'].deposit(300)
jordan.display_user_balance()

