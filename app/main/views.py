from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_movies,get_movie,search_movie,get_genres,get_similar_movies,get_genre_movies,get_collection
from .forms import ReviewForm,UpdateProfile
from ..models import Review, User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2

@main.route('/user/<uname>',methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user)

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    top_rated = get_movies('top_rated')

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search',movie_name=search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie,top_rated = top_rated)

@main.route('/genres')
def genres():
    genres = get_genres()
    return render_template('genres.html',genres = genres)

@main.route('/genres/<int:id>/movies')
def genre_movies(id):
    movies = get_genre_movies(id)
    return render_template('genre_movies.html',movies = movies)

@main.route('/collection/<int:id>')
def collection(id):
    collection = get_collection(id)
    return render_template('collection.html',collection = collection)

@main.route('/movie/<int:id>' ,methods = ['GET','POST'])
def movie(id):

    movie = get_movie(id)
    similar = get_similar_movies(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    form = ReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        user = current_user._get_current_object()
        new_review = Review(movie_id = movie.id,movie_title = title,image_path=movie.poster,movie_review=review,user = user)
        
        new_review.save_review()

        return redirect(url_for('.movie',id = movie.id ))

    return render_template('movie.html',title = title,movie = movie,similar = similar,reviews = reviews,review_form=form)

@main.route('/search/',methods=['GET'])
def search():
	keyword = request.args.get('q')
	keyword_list = keyword.split(" ")
	keyword_format = '%20'.join(keyword_list)
	searched_movies = search_movie(keyword_format)
	title = f'Search results for {keyword} '
	
	return render_template('search.html',movies = searched_movies)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname = user.username))
    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))

@main.route('/review/<int:id>')
def single_review(id):
    review = Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=['code-friendly','fenced-code-blocks'])
    return render_template('review.html',review=review,format_review=format_review)
