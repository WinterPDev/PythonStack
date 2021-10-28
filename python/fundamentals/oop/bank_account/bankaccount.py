

class bankAccount:
    instances=[]
    def __init__(self, name, int_rate=0.5, balance=0.00):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        bankAccount.instances.append(self)
    
    @classmethod
    def all_instances(cls):
        for i in cls.instances:
            print(i, i.name, i.int_rate, i.balance)
        return i

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

winter = bankAccount("Winter", 0.10)

winter.display_account_info()
# summer = bankAccount("Summer")

#  winter -> instance['winter'] 
# summer -> instances['winter','summer']
# print(i.balance -> winter.balance, i.balance -> summer.balance)

winter.deposit(100).deposit(100).deposit(100).yield_interest()
# summer.deposit(200).deposit(200).withdraw(100).withdraw(100).yield_interest().display_account_info()


bankAccount.all_instances()