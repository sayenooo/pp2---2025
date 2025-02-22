class Account:
    pass
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,cash):
        self.cash = cash
        self.balance+=self.cash
        print(f"{self.owner} deposited {self.cash}, new balance is {self.balance}")
    def withdraw(self,cash):
        self.cash = cash
        if(self.balance>self.cash):
            self.balance-=self.cash
            print(f"{self.owner} withdrew {self.cash}, new balance is {self.balance}")
        else:
            print("Error, check your balance pls!")

Owner = input()
Balance =  int(input())

account = Account(Owner,Balance)

account.deposit(int(input()))
account.withdraw(int(input()))