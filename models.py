from datetime import datetime
from ncaa import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    passwordHash = db.Column(db.String(128))
    bets = db.relationship('Bet', backref='Bettor', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(64), index=True)
    betDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Team: {}|Bet Date: {}>'.format(self.teamName, self.betDate)

