from flask import Flask, render_template, url_for, redirect
from flask import request
import sys,time,random
import pickle 
from game_engine import Game
import hero


app = Flask (__name__)


def get_input(valid_input: list, input):#get user input
  while True:
    user_entered = input #user input goes here
    if user_entered not in valid_input:
      print("Invalid input. Please use one \
              of the following inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered


def display_page_text(lines: list):
  for line in lines:
    storyline = []
    storyline.append(line)
  return storyline  #print story lines

def getoptionline(optionline):
  return optionline


def get_response(options: list, hero1, input):
  for index, option in enumerate(options):
    optionline = (str(index) + ". " + option[0])  #print options
    
  valid_inputs = [str(num) for num in range(2)]

  option_index = int (get_input(valid_inputs, input))
  hero1.primary_increase(options[option_index][2])
  if options[option_index][3] != None:
   hero1.secondary_increase(options[option_index][3])
  
  return options[option_index][1]


def story_flow(story: dict, hero1, input):
  curr_page = 1

  if curr_page != None:
    page = story.get(curr_page, None)
    
    if page == None:
      curr_page = None
      #break

    storyline = display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      hero1.get_dict()
      hero1.final_score()
      #break

    curr_page = get_response(page['Options'], hero1, input)
    return storyline


@app.route('/', methods = ['POST', 'GET'])
def index():
  if request.method=='POST':
    user = request.form["name"]
    story = "story begins here"
    return render_template("adventure.html", name = user, story_line = story)
  else:
    user = request.args.get("name")
    return render_template('index.html')

@app.route('/adventure', methods = ['POST', 'GET'])
def adventure():
  hero1 = hero.Hero("name")
  story = {}
  with open('chapter1.ch', 'rb') as chapter:
    story = pickle.load(chapter)
  if request.method == 'POST':
    choice = request.form["choice"]
    storyline = story_flow(story, hero1, choice)
    return render_template('adventure.html', story_line = storyline)
    #return "You have chosen" + " " + choice
  else:
    choice = request.args.get("choice")
    storyline = story_flow(story, hero1, choice)
    return render_template('adventure.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

   