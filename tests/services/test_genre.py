import pytest

from unittest.mock import MagicMock

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService



@pytest.fixture()
def genre_dao():
    genre_instance = GenreDAO(None)

    g1 = Genre(id=1, name='horror')
    g2 = Genre(id=2, name='adventure')

    genre_instance.get_one = MagicMock(return_value=g1)
    genre_instance.get_all = MagicMock(return_value=[g1, g2])
    genre_instance.create = MagicMock(return_value=Genre(id=5))
    genre_instance.delete = MagicMock()
    genre_instance.update = MagicMock()
    return genre_instance

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()

        assert len(genre) > 0

    def test_creat(self):
        genre_data = {
            'name': 'Ivan'
        }

        genre = self.genre_service.create(genre_data)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_data = {
            'name': 'kiril'
        }
        self.genre_service.update(genre_data)