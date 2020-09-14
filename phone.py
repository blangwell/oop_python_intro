class Phone():
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print('Calling {} from {}'.format(other_number, self.number))
  
  def text(self, other_number, msg):
    print('Sending text to {} from {}'.format(other_number, self.number))
    print(msg)

  def open_app(self, app_name):
    print('Opening {} on device'.format(app_name))

# subclass of Phone
class Iphone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.fingerprint = None

  def set_fingerprint(self, new_fingerprint):
    self.fingerprint = new_fingerprint
  
  # note, fingerprint below is not referring to line 19
  def unlock(self, fingerprint=None):
    if (fingerprint == None and self.fingerprint == None):
      print('phone is unlocked because no fingerprint is currently set')

    if (fingerprint == self.fingerprint):
      print('Phone is unlocked')
    else: 
      print('Phone locked, Fingerprint does not match')

martin_iphone = Iphone(5551112222)
print('martin\'s number is {}'.format(martin_iphone.number))

martin_iphone.set_fingerprint('password')
print(martin_iphone.fingerprint)

martin_iphone.unlock('password123')

# here we use the call method inherited from Phone parent class
martin_iphone.call(2224449999)

martin_iphone.open_app('tik tok')