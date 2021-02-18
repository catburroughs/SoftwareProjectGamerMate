from flask import Flask, render_template, url_for, redirect
from flask import request
import sys,time,random
import pickle 
from game_engine import Game
#import hero


app = Flask (__name__)



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
  if request.method == 'POST':
    choice = request.form["choice"]
    story = "story continues here"
    return render_template('adventure.html', story_line = story)
    #return "You have chosen" + " " + choice
  else:
    choice = request.args.get("choice")
    return render_template('adventure.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

   