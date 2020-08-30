import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestMovie:
    def test_model(self):
        obj = mixer.blend('tutorial.Movie')
        assert obj.pk == 1, 'Should create a Post instance'

    def test_movie_name(self):
        obj = mixer.blend('tutorial.Movie', name="Dil bechara")
        assert obj.name == "Dil bechara", 'Should return movie name'
