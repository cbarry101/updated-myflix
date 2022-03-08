from operator import ge
from flask import Flask, render_template, redirect, url_for, request,flash
from model import *
from flask_login import login_user, login_required, current_user, LoginManager,logout_user
#from main import app
from connect import search_movie,get_movie_name_by_id


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(users_info_id):
    return Users_info.query.get(users_info_id)

#Home
@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register', methods=['GET'])
def new_user():
    return render_template('register.html')

@app.route('/new')
def profile():
    return render_template('profile.html')


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    password = request.form["password"]
    username = request.form["username"]


    new_user = Users_info(password=password, username=username)

    db.session.add(new_user)
    db.session.commit()

    flash(f"User {new_user.username} added.")
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    '''Logs the user in and checks user exists'''
    user = Users_info.query.filter_by(username = request.form['username']).first()
    
    if user:
        if user.password == request.form['password']:
            login_user(user)
            return render_template('/profile.html')
        else:
            return 'Doesnt match our login'
    else:
        return 'Doesnt match our login'
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/home')

@app.route('/search', methods=['POST'])
@login_required
def search():
    user_search = search_movie(request.form['movie'])
    return render_template('/movies.html', movies=user_search)
    

@app.route('/add', methods=['POST'])
@login_required
def add_movie():
    movie_id = request.form['movie_id']
    movie_list = Watch_list(users_info_id=current_user.users_info_id, movie_id=movie_id)

    db.session.add(movie_list)
    db.session.commit()
    return render_template('/profile.html')

@app.route('/watch_list', methods=['GET'])
@login_required
def get_watch_list():
    watch_list_results = Watch_list.query.filter_by(users_info_id=current_user.users_info_id).all()
    name_list = []
    for watched in watch_list_results:
        movie_id = watched.movie_id
        movie_info = get_movie_name_by_id(movie_id)
        name_list.append(movie_info)
    return render_template('your_movies.html', name_list=name_list) 


@app.route('/watched_movies', methods=['GET','POST'])
@login_required
def get_watched_movies():
    if request.method=='POST':
        movie_id = request.form['movie_id']
        print(movie_id)
        print(type(movie_id))
        movie_to_delete = Watch_list.query.filter_by(users_info_id=current_user.users_info_id, movie_id=movie_id).first()
        new_watched_movie = Watched_movies(users_info_id=current_user.users_info_id, movie_id=movie_id, movie_rating=0)
        db.session.add(new_watched_movie)
        db.session.commit()
        db.session.delete(movie_to_delete)
        db.session.commit()
        all_watched_movies = Watched_movies.query.filter_by(users_info_id=current_user.users_info_id).all()
        all_watched_movies_list = []
        for watched_movie in all_watched_movies:
            movie_title = get_movie_name_by_id(watched_movie.movie_id)
            all_watched_movies_list.append(movie_title)
        return render_template('watched_movies.html', all_watched_movies_list=all_watched_movies_list)
    else:
        all_watched_movies = Watched_movies.query.filter_by(users_info_id=current_user.users_info_id).all()
        all_watched_movies_list = []
        for watched_movie in all_watched_movies:
            movie_title = get_movie_name_by_id(watched_movie.movie_id)
            all_watched_movies_list.append(movie_title)
        return render_template('watched_movies.html', all_watched_movies_list=all_watched_movies_list)


@app.route('/get_overview', methods=['POST'])
@login_required
def get_movie_overview():
    movie_overview = request.form['movie_overview']
    print(movie_overview)
    print(type(movie_overview))
    return render_template('movie_overview.html', movie_overview=movie_overview)
        
