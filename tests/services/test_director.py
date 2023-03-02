import pytest

from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService



@pytest.fixture()
def director_dao():
    director_instance = DirectorDAO(None)

    d1 = Director(id=1, name='max')
    d2 = Director(id=2, name='jonh')

    director_instance.get_one = MagicMock(return_value=d1)
    director_instance.get_all = MagicMock(return_value=[d1, d2])
    director_instance.create = MagicMock(return_value=Director(id=5))
    director_instance.delete = MagicMock()
    director_instance.update = MagicMock()
    return director_instance

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_creat(self):
        director_data = {
            'name': 'Ivan'
        }

        director = self.director_service.create(director_data)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_data = {
            'name': 'kiril'
        }
        self.director_service.update(director_data)
