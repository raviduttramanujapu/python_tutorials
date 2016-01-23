class Person:
  # Variables
  # Functions

  def __init__(self, name, initial_deposit):
    # print 'initialized'
    self.name = name
    self.initial_deposit = initial_deposit
    self.balance = initial_deposit
    self.__total_accounts = 10001

  def current_balance(self):
    return self.balance

  def total_accounts(self):
    print  self.__total_accounts

  def withdraw(self, amount):
    self.balance = self.balance - int(amount)
    return self.balance

  def deposit(self, amount):
    self.balance = self.balance + int(amount)

  def __del__(self):
    pass
    # print 'This instance is deleted; will not exists anymore'

