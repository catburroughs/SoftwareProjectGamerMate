import pickle

class Hero:
  
  def __init__(self, name):
    self.name = name
    self.attributes = {'risky':0, 'safe':0, 'indie':0, 'group':0 }
    

  def primary_increase(self, attribute):
    if attribute in self.attributes:
      self.attributes[attribute] += 25

  def secondary_increase(self, attribute):
    if attribute in self.attributes:
      self.attributes[attribute] += 15

  def get_dict(self):
    print(self.attributes)

  def final_score(self):
    self.final_values = sorted(self.attributes, key = self.attributes.get, reverse = True)
    for x in self.final_values:
      print(x, self.attributes[x])

    


