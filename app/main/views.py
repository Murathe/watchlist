from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies, get_movie, search_movie
from .models import review
from .forms import ReviewForm
Review = review.Review

@main.route('/')
def index():
    '''
    View root page that returns index file and its data
    '''
    # Popular movies fetch
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    playing_movie = get_movies('now_playing')
    title = 'Home - Welcome to your home of all news'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', title = title,popular = popular_movies,upcoming = upcoming_movies,now_playing = playing_movie)

@main.route('/movie/<int:id>')
def movie(id):
    '''
    Page that loads movie page and more data on it
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html', title = title, movie = movie, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display search results
    '''
    movie_name_list = movie_name.split("")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id))

    title - f'{movie.title} review'
    return render_template('new_review.html', title = title, review_form = form, movie = movie)

