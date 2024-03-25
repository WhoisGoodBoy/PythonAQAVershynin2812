import pytest
from lesson25.infrastructure import Phone, Dog





@pytest.fixture
def phone():
    yield Phone()

@pytest.fixture
def dog():
    yield Dog


@pytest.fixture
def dog_pack():
    yield Dog.genreate_dogs_pack()

