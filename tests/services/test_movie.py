import pytest

from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService



@pytest.fixture()
def movie_dao():
    movie_instance = MovieDAO(None)

    m1 = Movie(id=1, title='max', description='123', trailer='trailer', year=1996, rating=13.9, genre_id=1, director_id=1)
    m2 = Movie(id=2, title='john', description='123667', trailer='trailer776665', year=2008, rating=23.9, genre_id=1, director_id=1)

    movie_instance.get_one = MagicMock(return_value=m1)
    movie_instance.get_all = MagicMock(return_value=[m1, m2])
    movie_instance.create = MagicMock(return_value=Movie(id=5))
    movie_instance.delete = MagicMock()
    movie_instance.update = MagicMock()
    return movie_instance

class TestMovieService:

    @pytest.fixture(autouse=True)
    def director_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_creat(self):
        movie_data = {
            "title": "asda",
            "description": "333",
            "trailer": "trailer 1",
            "year": 1969,
            "rating": 8.3,
            "genre_id": 21,
            "director_id": 33
        }

        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_data = {
            'name': 'kiril'
        }
        self.movie_service.update(movie_data)