class MartialArts():
  def __init__(self, name, type_of):
    self.name = name
    self.type_of = type_of
    self.score = 0
    self.blurb = ''

  def add_score(self, user_score):
    self.score += user_score
    print(f'Your score for {self.name} is {user_score} / 10')

  def add_blurb(self, user_blurb):
    self.blurb = user_blurb
    print('Here is your blurb for {} :\n{}'.format(self.name, self.blurb))
  
  def rename(self, new_name):
    self.name = new_name
    print('The new name is {}'.format(new_name))

karate = MartialArts('karate', 'hard style')
karate.add_score(7)
karate.add_blurb('Cobra kai is pretty sick')

karate.rename('Cool guy club')

taichi = MartialArts('tai chi', 'soft style')
taichi.add_score(9)
taichi.add_blurb('Tai chi makes me feel better')