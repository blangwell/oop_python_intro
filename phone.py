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

# martin_iphone.set_fingerprint('password')
# print(martin_iphone.fingerprint)
# martin_iphone.unlock('password123')
# # here we use the call method inherited from Phone parent class
# martin_iphone.call(2224449999)
# martin_iphone.open_app('tik tok')


class Android(Phone):
  # initialize an instance of Android class
  def __init__(self, phone_number):
    # inherit from Phone parent class to access its methods
    # we pass in phone number because parent Phone class needs access 
    super().__init__(phone_number)
    self.keyboard = 'Default'

  # string representation of an object
  def __str__(self):
    return 'this phone is owned by {}'.format(self.number)

  def set_keyboard(self, new_keyboard):
    self.keyboard = new_keyboard

Android.ORIGIN = Android('')

josh_phone = Android(5557130000)
josh_phone.set_keyboard('Dvorak')
josh_phone.call(8298111141)

josh_phone.open_app('google play store')
print(josh_phone)