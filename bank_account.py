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
  def __init__(self, kind):
    self.balance = 0
    self.overdraft_fees = 0

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

    if self.balance < 0 :
      self.overdraft_fees += 36
    return amount