# class BankAccount(): 
#   def __init__(self, kind):
#     self.kind = kind
#     self.balance = 0
  
#   def deposit(self, amount):
#     print(f'you deposited {amount} dollars\n your remaining balance is {self.balance}')
#     return self.balance = self.balance + amount
    
#   def withdraw(self, amount): 
#     print('withdraw')
#     if amount > self.balance:
#       print('insufficient funds')
#     else:
#       print(f'you withdrew {amount} dollars \n your remaining balance is {self.balance}')
#       return self.balance -= amount

# barent_bank = BankAccount('checking')
# print(barent_bank.kind)

class BankAccount():
  def __init__(self, kind, pin):
    self.balance = 0
    self.overdraft_fees = 0
    self.kind = kind
    self.pin = pin

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount, pin_from_user):
    
    if (self.pin == pin_from_user):
      if (self.balance < amount):
        print('sorry, you don\'t have that amount in your account.')
        return 
      elif (self.balance == amount):
        self.balance -= amount
        print('no more money buddy - big broke')
      else:
        self.balance -= amount
        print('current balance is now ${}'.format(self.balance))
    else:
      print('invalid pin, try again ')

  def change_pin(self, pin):
    self.pin = pin
    print(f'the new pin number is {self.pin}')


barent_checking = BankAccount('checking', 1234)
# print('my new account is a {} account'.format(barent_checking.kind))

barent_checking.deposit(3000)
# print('my current balance is ${}.'.format(barent_checking.balance))

barent_checking.withdraw(1500, 2333)
print('my current balance is ${}.'.format(barent_checking.balance))

barent_checking.withdraw(2000, 1234)
print('my overdraft fee is currently ${}'.format(barent_checking.overdraft_fees))

# barent_checking.change_pin(5678)