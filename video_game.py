class VideoGame():
  def __init__(self, title, esrb, year):
    self.title = title
    self.esrb = esrb
    self.year = year
    self.score = 0
  
  def score_game(self, user_score):
    self.score += user_score
    print('You rated {} a {} out of 10'.format(self.title, self.score))
  
  def show_rating(self):
    print('{} is rated {} by the ESRB'.format(self.title, self.esrb))

  def show_year(self):
    print('{} was released in {}'.format(self.title, self.year))

sekiro = VideoGame('sekiro', 'M', '2019')

sekiro.score_game(9)
sekiro.show_rating()
sekiro.show_year()