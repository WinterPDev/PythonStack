from bankaccount import bankAccount

class User: 
    def __init__(self, user_name):
        self.user_balance = bankAccount(int_rate=0.02, balance=0)
        self.user_name = user_name

    def make_deposit(self,amount):
        self.user_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.user_balance -= amount
        return self

    def transfer_money(self,receiver,amount):
        self.make_withdrawal(amount)
        receiver.make_deposit(amount)
        print(f"User {self.user_name} Transfered {amount} to {receiver.user_name}.\n User: {self.user_name} Balance: {self.user_balance} \n User: {receiver.user_name} Balance: {receiver.user_balance}")
        return self, receiver

    def display_user_balance(self):
        print("User:" + self.user_name + " Balance:" + str(self.user_balance))
        return self


winter = User("Winter")
summer = User("Summer")
autumn = User("Autumn")
spring = User("Spring")

winter.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()

summer.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

autumn.make_deposit(300).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

winter.transfer_money(autumn,50)