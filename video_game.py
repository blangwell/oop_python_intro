class VideoGame():
  def __init__(self, title, esrb, year):
    self.title = title
    self.esrb = esrb
    self.year = year
    self.score = 0
    self.blurb = ''

  def score_game(self, user_score):
    self.score += user_score
    print('You rated {} a {} out of 10'.format(self.title, self.score))
  
  def show_rating(self):
    print('{} is rated {} by the ESRB'.format(self.title, self.esrb))

  def show_year(self):
    print('{} was released in {}'.format(self.title, self.year))

  def add_blurb(self, blurb):
    self.blurb = blurb
    print('here is your blurb about {}: \n{}'.format(self.title, blurb))
  

sekiro = VideoGame('sekiro', 'M', '2019')

# sekiro.score_game(9)
# sekiro.show_rating()
# sekiro.show_year()
# sekiro.add_blurb('this game is super fun i say!')

dark_souls_3 = VideoGame('Dark Souls 3', 'M', '2016')
dark_souls_3.add_blurb('super fun stuff. have a panic attack! ')