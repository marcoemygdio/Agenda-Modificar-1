from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  phone = db.Column(db.String())
  image = db.Column(db.String())
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

@app.route('/')
def index():
  contacts = Contacts.query.all()
  return render_template('index.html', contacts=contacts)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  new_name = Contacts(name=name)
  db.session.add(new_name)
  db.session.commit()
  return redirect('/')
  

if __name__ == "__main__":
  db.create_all()
  app.run(host='0.0.0.0', port=8080)