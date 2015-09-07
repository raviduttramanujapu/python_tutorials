
class Person:
  # Variables
  # Functions

  def __init__(self, name, initial_deposit):
    self.name = name
    self.initial_deposit = initial_deposit
    self.balance = initial_deposit

  def current_balance(self):
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - int(amount)
    return self.balance

  def deposit(self, amount):
    self.balance = self.balance + int(amount)