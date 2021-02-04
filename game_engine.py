import sys,time,random
import pickle 
from hero import *

def slow_type(t):
    typing_speed = 150 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


def get_input(valid_input: list):
  while True:
    user_entered = input()
    if user_entered not in valid_input:
      print("Invalid input. Please use one \
              of the following inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered


def display_page_text(lines: list):
  for line in lines:
    slow_type(line)
    # Make the user press enter to see the next line
    #get_input([""])


def get_response(options: list):
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
  
  valid_inputs = [str(num) for num in range(4)]

  option_index = int(get_input(valid_inputs))

  #print(options[option_index][3])
  hero1.primary_increase(options[option_index][2])
  if options[option_index][3] != None:
    hero1.secondary_increase(options[option_index][3])
  
  return options[option_index][1]


def story_flow(story: dict):
  curr_page = 1

  while curr_page != None:
    page = story.get(curr_page, None)
    
    if page == None:
      curr_page = None
      break

    display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      break

    curr_page = get_response(page['Options'])
   
if __name__=='__main__':
    hero1 = Hero('jim')
    story = {}
    with open('chapter1.ch', 'rb') as chapter:
 
        story = pickle.load(chapter)

    story_flow(story)
    hero1.get_dict()
    hero1.final_score()
