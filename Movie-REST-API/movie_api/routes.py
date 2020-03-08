from flask import jsonify, Blueprint

from movie_api import db


main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    ''' Adds movies to the database '''

    return 'Movie was added successfully', 201


@main.route('/movies')
def movies():
    ''' Returns a list of movies in the database '''

    movies = list()
    return jsonify({'movies': movies})