from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from main import app, db, connect_to_db
from flask_login import UserMixin



class Users_info(db.Model, UserMixin):
    """Users of Myflix app."""

   

    users_info_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    def get_id(self):
        return(self.users_info_id)

class Watched_movies(db.Model):
    """Watched movies of MyFlix."""



    watched_movies_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    movie_rating = db.Column(db.Integer, nullable=False)
    users_info_id = db.Column(db.Integer, db.ForeignKey('users_info.users_info_id'))


class Watch_list(db.Model):
    '''Watch list for MyFlix'''
    watch_list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    users_info_id = db.Column(db.Integer, db.ForeignKey('users_info.users_info_id'))
    movie_id=db.Column(db.Integer, nullable=False)




if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from main import app
    connect_to_db()
    print("Connected to DB.")

    
