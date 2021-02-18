import sys,time,random
import pickle 
import hero

class Game:
  def __init__(self):
    self.story = {}
    self.hero1 = hero.Hero("jim")


    

  def slow_type(self, t):
      typing_speed = 150 #wpm
      for l in t:
          sys.stdout.write(l)
          sys.stdout.flush()
          time.sleep(random.random()*10.0/typing_speed)
      print('')


  def get_input(self, valid_input: list):
    while True:
      user_entered = input()
      if user_entered not in valid_input:
        print("Invalid input. Please use one \
                of the following inputs:\n")
        print(valid_input)
        user_entered = None
      else:
        return user_entered


  def display_page_text(self, lines: list):
    for line in lines:
      self.slow_type(line)
      # Make the user press enter to see the next line
      #get_input([""])


  def get_response(self, options: list):
    for index, option in enumerate(options):
      print(str(index) + ". " + option[0])
    
    valid_inputs = [str(num) for num in range(2)]

    option_index = int(self.get_input(valid_inputs))

    #print(options[option_index][3])
    self.hero1.primary_increase(options[option_index][2])
    if options[option_index][3] != None:
      self.hero1.secondary_increase(options[option_index][3])
    
    return options[option_index][1]


  def story_flow(self, story: dict):
    curr_page = 1

    while curr_page != None:
      page = story.get(curr_page, None)
      
      if page == None:
        curr_page = None
        break

      self.display_page_text(page['Text'])
      
      if len(page['Options']) == 0:
        curr_page = None
        self.hero1.get_dict()
        self.hero1.final_score()
        break

      curr_page = self.get_response(page['Options'])
    
    
    
# def run():
#   newGame = Game()
#   hero1 = hero.Hero('jim')
#   newGame.story = {}
#   with open('chapter1.ch', 'rb') as chapter:
#     story = pickle.load(chapter)

#   newGame.story_flow(story)
#   hero1.get_dict()
#   hero1.final_score()
