from bankaccount import bankAccount

class User: 
    def __init__(self, user_name):
        self.user_name = user_name
        self.account = bankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self

    def transfer_money(self,receiver,amount):
        self.account.withdraw(amount)
        receiver.account.deposit(amount)
        print(f"User {self.user_name} Transfered {amount} to {receiver.user_name}.\n User: {self.user_name} Balance: {self.account.balance} \n User: {receiver.user_name} Balance: {receiver.account.balance}")
        return self, receiver

    def display_user_balance(self):
        print("User:" + self.user_name + " Balance:" + str(self.account.balance))
        return self


winter = User("Winter")
winter_2 = User("Winter2")
summer = User("Summer")
autumn = User("Autumn")
spring = User("Spring")

winter.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()

summer.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

autumn.make_deposit(300).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

winter.transfer_money(autumn,50)

winter.transfer_money(winter_2, 20)