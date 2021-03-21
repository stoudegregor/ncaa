from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #render_template('home.html')
    return 'Home Page'

@app.route('/schedule')
def schedule():
    return 'Games Scheduled'

@app.route('/teams')
def teams():
    return 'All Teams'

@app.route('/bets')
def bets():
    return 'Bets page'

@app.route('/bets/newBet')
def newBet():
    return 'Submit Bet form'

@app.route('/users/<username>')
def getProfile(username):
    return '{}\'s profile'.format(escape(username))

