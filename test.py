from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask, render_template, redirect, url_for, flash, abort
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    pets = relationship('Pets', back_populates="name")
class Pets(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = relationship('Owners', back_populates='pets')
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))


db.create_all()
@app.route("/")
def home():
    benji = Pets.query.get(id=1)
    return render_template("testindex.html", pet=benji)
if __name__ == "__main__":
    app.run(debug=True)