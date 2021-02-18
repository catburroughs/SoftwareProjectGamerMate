import pickle

class Hero:
  
  def __init__(self):
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
    final_values = sorted(self.attributes, key = self.attributes.get, reverse = True)
    s = ""
    for x in final_values:
      s += x + ": " + str(self.attributes[x]) + "<br>"

    return s



    


