

class User: 
    def __init__(self, user_name):
        self.user_balance = 0
        self.user_name = user_name

    def make_deposit(self,amount):
        self.user_balance += amount
        return self.user_balance    

    def make_withdrawal(self,amount):
        self.user_balance -= amount
        return self.user_balance

    def transfer_money(self,receiver,amount):
        self.user_balance -= amount
        receiver.user_balance += amount
        return self.user_balance, receiver.user_balance
    
    def display_user_balance(self):
        display = print("User:" + self.user_name + " Balance:" + str(self.user_balance))
        return display

winter = User("Winter")
summer = User("Summer")
autumn = User("Autumn")
spring = User("Spring")

# winter.user_name = "Winter"

User.make_deposit(winter, 100)
User.make_deposit(winter, 100)
User.make_deposit(winter, 100)
User.make_withdrawal(winter,100)
User.display_user_balance(winter)

User.make_deposit(summer, 100)
User.make_deposit(summer, 100)
User.make_withdrawal(summer,100)
User.make_withdrawal(summer,100)
User.display_user_balance(summer)

User.make_deposit(autumn, 300)
User.make_withdrawal(autumn, 100)
User.make_withdrawal(autumn, 100)
User.make_withdrawal(autumn, 100)
User.display_user_balance(autumn)

User.transfer_money(winter,autumn,50)
User.display_user_balance(winter)
User.display_user_balance(autumn)
