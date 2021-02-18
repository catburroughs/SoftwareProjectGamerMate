from flask import Flask, render_template, url_for, request
import sys,time,random
import pickle 
from game_engine import Game
#import hero


app = Flask (__name__)

@app.route('/', methods = ['POST', 'GET'])

def index():
  newGame = Game()
  newGame.story = {}
  with open('chapter1.ch', 'rb') as chapter:
    story = pickle.load(chapter)
    newGame.story_flow(story)
  if request.method == 'POST':
      valid_inputs = request.form.get('valid_inputs')
      return valid_inputs
  return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True, port=5000)

   