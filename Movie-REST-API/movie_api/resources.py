from flask import jsonify, request, Blueprint

from movie_api import db
from movie_api.models import MovieModel


main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    ''' Adds movies to the database '''

    movie_data = request.get_json()
    movie = MovieModel.find_by_title(movie_data['title'])
    if movie:
        return {'message': f"A movie with the title '{movie.title}' already exists!"}, 400

    new_movie = MovieModel(title=movie_data['title'], rating=movie_data['rating'])

    try:
        new_movie.save_movie_to_db()
    except:
        return {'message': f"An error occured."}, 500

    return f"Movie with title '{new_movie.title}' was added successfully!", 201


@main.route('/update_movie/<title>', methods=['PUT', 'POST'])
def update_movie(title: str):
    movie_data = request.get_json()
    movie = MovieModel.find_by_title(title)

    if movie:
        try:
            movie.title = movie_data['title']
            movie.rating = movie_data['rating']
            movie.save_movie_to_db()
        except:
            return {'message': f"An error was encountered whilst updating this movie"}, 500
    else:
        try:
            movie = MovieModel(title, **movie_data)
        except:
            return {'message': f"An error was encountered whilst inserting this movie."}, 500
    return jsonify({'movie': movie}), 200


@main.route('/delete_movie/<title>', methods=['DELETE'])
def delete_movie(title: str):
    movie = MovieModel.find_by_title(title)

    if movie:
        movie.delete_movie()
        return {'message': 'Movie deleted successfully!'}
    
    return {'message': 'Movie not found.'}, 404


@main.route('/movies')
def movies():
    ''' Returns a list of movies in the database '''

    movie_list = MovieModel.find_all()
    movies = list()

    for movie in movie_list:
        movies.append({'title': movie.title, 'rating': movie.rating})
    return jsonify({'movies': movies}), 200