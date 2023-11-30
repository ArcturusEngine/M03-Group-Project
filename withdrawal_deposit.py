class Person:
     def __init__(self, f_name, l_name):
          self.f_name = str
          self.l_name = str
          self.name = f"{self.f_name} {self.l_name}"

class Account:
    "A class containing all accounts and methods for giving loans, depositing, & withdrawing money into accounts"
    def __init__(self, person: Person):
         self.balance = 0
         self.person = person

    def withdraw(self, amt: int):
        print(f"{self.person.name}, Your current balance is: {self.balance}\n\n")
        
        try:
            amt = int(input("Please enter the amount you wish to withdraw: "))
            if self.balance > amt > 0:
                self.balance = amt - self.balance
                confirm = chr(input(f"You are requesting to withdraw { amt}, is that correct? (Y/N): "))
                if confirm.capitalize() == "Y":
                    print(f"Your new self.balance is: {self.balance}. Thank you.")
            elif self.balance <= 0 < amt:
                print(f"You are unable to withdraw money with no money or debt. Request denied.")
            elif amt > self.balance > 0:
                print("You are unable to withdraw more than you current self.balance. Request denied.")
            else:
                print(f"I'm sorry, We cannot process your withdrawal request.")
        except TypeError: 
            print("We're sorry, you are unable to withdraw this amount.")

    def deposit(self, amt: int):
        print(f"Your current self.balance is: {self.balance}")
        try:
            amt = int(input("Please enter the amount that you wish to deposit: "))
            if amt > 0:
                    confirm = chr(input(f"You are requesting to deposit {amt}, is that correct? (Y/N): "))
                    if confirm.capitalize() == "Y":
                        self.balance += amt
                        print(f"Your new self.balance is: {self.balance}. Thank you.")
                    elif confirm.capitalize() == "N":
                         print("Your request has been cancelled")
            elif amt < 0:
                    print(f"You are unable to deposit values less than zero. Request denied.")
            else:
                    print(f"I'm sorry, We cannot process your deposit request.")
        except TypeError:
            print("We're sorry, you are unable to deposit this amount.")


class Bank:
    "A class that makes bank accounts out of the information of the Person class"
    def __init__(self):
        self.accounts: {str: Account} = []

    def get_account(self, account_holder_name: str):
        return self.accounts[account_holder_name.lower()]

    def create_account(self, person: Person, ):
          account = Account(person)
          self.accounts[person.name.lower()] = account
person1 = Bank.create_account(Person("Bryce", "Bland"))
