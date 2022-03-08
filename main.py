from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:concondk123@localhost:5432/myflixdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'the random string'



db = SQLAlchemy(app)


def connect_to_db():
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    connect_to_db()
    from views import *
    app.run(debug=True)