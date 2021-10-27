

class bankAccount:
    instances=[]
    def __init__(self,int_rate=0.5, balance=0.00):
        self.int_rate = int_rate
        self.balance = balance
        bankAccount.instances.append(self)
    
    @classmethod
    def all_instances(cls):
        print(cls.instances)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance:" + "$" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance != 0.00:
            self.balance += self.balance * self.int_rate
        return self



winter = bankAccount()
summer = bankAccount()

winter.deposit(100).deposit(100).deposit(100).yield_interest()
summer.deposit(200).deposit(200).withdraw(100).withdraw(100).yield_interest().display_account_info()


bankAccount.all_instances()