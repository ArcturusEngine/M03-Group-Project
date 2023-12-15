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
    self._balance -= amount
    
    if amount > 0 and self._balance >= amount:
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
    self.accounts[person.full_name.lower(
    )] = account  # Add account to the dictionary with the person's name as key


traffic = "red"
while traffic == "red":
  bank = Bank()  # Create a Bank object
  first_name = input(str("Enter your first name: ").title())
  last_name = input(str("Enter your last name: ").title())
  bank.create_account(
      first_name,
      last_name)  # Create an account for a person with the given name
  person_name = (f"{first_name} {last_name}")

  account = bank.get_account(person_name)
  try:
    if account:
      print(f"Account found for {person_name}: Balance - {account.balance}")
      traffic = "green"
  except:
    print("Account not found")

  while True:
    try:
      print("1. Deposit")
      print("2. Withdraw")
      print("3. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
        amount = int(input("Enter the amount to deposit: "))
        if account.deposit(amount):
          print(f"Deposit successful. New balance: {account.balance}")
          print(f"{amount} deposited successfully")
        else:
          print("Invalid amount")
      elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if account.withdraw(amount):
          print(f"{amount} withdrawn successfully")
          print(f"New balance: {account.balance}")
      elif choice == 3:
        print(f"Account found for {person_name}: Balance - {account.balance}")
        print("Good bye")
        break
    except:
      print("you can't do that")
