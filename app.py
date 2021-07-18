from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database@localhost/login'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AccountInfo (db.Model):
    __tablename__ = 'accountInfo'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    dateOfBirth = db.Column(db.DateTime())
    favoriteColor = db.Column(db.String())
    hobby = db.Column(db.String())

    def __init__(self, email, password, dateOfBirth, favoriteColor, hobby):
        self.email = email
        self.password = password
        self.dateOfBirth = dateOfBirth
        self.favoriteColor = favoriteColor
        self.hobby = hobby

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signUp.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    return render_template('loggedIn.html')

@app.route('/createAccount', methods=['POST'])
def createAccount():
    email = request.form['email']
    password = request.form['password']
    dateOfBirth = request.form['dateOfBirth']
    hobby = request.form['hobby']
    color = request.form['color']
    print(email, password, dateOfBirth, hobby, color)
    if db.session.query(AccountInfo).filter(AccountInfo.email == email).count() == 0:
        data = AccountInfo(email, password, dateOfBirth, hobby, color)
        db.session.add(data)
        db.session.commit()
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run()