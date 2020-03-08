from dataclasses import dataclass

from movie_api import db

@dataclass
class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    title: str
    rating: float

    @classmethod
    def find_by_title(cls, title: str):
        ''' Retrieve data by title. '''

        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls):
        ''' Retrieve all data in the database. '''

        return cls.query.all()

    def save_movie_to_db(self):
        ''' Store movie data to the database. '''

        db.session.add(self)
        db.session.commit()

    def delete_movie(self):
        ''' Delete movie data from the database. '''

        db.session.delete(self)
        db.session.commit()