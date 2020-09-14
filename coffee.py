class CoffeeCup(): 
    # in javascript we say this, in python it is self
    # constructor function
  def __init__(self, capacity):
    self.capacity = capacity
    self.amount = 0
  
  def fill(self):
    self.amount = self.capacity
  
  def empty(self):
    self.amount = 0

  def drink(self, amount):
    self.amount -= amount
    if (self.amount == 0):
      self.amount = 0
      print('The cup is currently empty')