class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


class Account:
    def __init__(self, person):
        self._person = person
        self._balance = 0

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    @property
    def balance(self):
        return self._balance

    @property
    def person_name(self):
        return self._person.full_name


class Bank:
    def __init__(self):
        self.accounts = {}  # Create an empty dictionary to store accounts

    def get_account(self, account_holder_name):
        return self.accounts.get(account_holder_name.lower(), "Account not found")

    def create_account(self, first_name, last_name):
        person = Person(first_name, last_name)  # Create a Person object
        account = Account(person)  # Create an Account object with the person
        self.accounts[person.full_name.lower()] = account  # Add account to the dictionary with the person's name as key


bank = Bank()  # Create a Bank object
person_name = input("Please enter your first and last name: ")
bank.create_account("Bryce", "Bland")  # Create an account for a person with the given name
account = bank.get_account(person_name)
if account:
    print(f"Account found for {person_name}: Balance - {account.balance}")
else:
    print("Account not found")


