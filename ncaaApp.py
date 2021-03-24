from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    user = {'username': 'Byron'}
    bets = [
            {
                'teamName': 'Michigan',
                'betDate': '3/22/2021',
                'betAmount': 20,
                'betResult': 'Dubs'
            },
            {
                'teamName': 'Florida State',
                'betDate': '3/22/2021',
                'betAmount': 20,
                'betResult': 'Dubs'
            }
        ]
    return render_template('home.html', title='Bets', user=user, bets=bets)
