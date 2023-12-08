class BankAccount:
    
    
    def __init__(self, int_rate=0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: charging a $5 fee")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
        
class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

account1 = BankAccount()
account2 = BankAccount(0.02,400)

User1 = User('Steve Martin', 'funnysteve@comedy.com', account1)

User1.make_deposit(500).make_withdraw(300).display_user_balance()

print(User1.account.balance)