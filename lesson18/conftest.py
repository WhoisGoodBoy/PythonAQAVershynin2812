import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lesson15.len_dict_example import Building, Company


@pytest.fixture
def building():
    print('I`m creating building')
    yield Building('Twice Tower', 'Myloslavska 65')

@pytest.fixture
def openai_company():
    yield Company('OpenAI', 'artificial intelligence')

@pytest.fixture
def nails_company():
    yield Company('Best Nails', 'beauty')

@pytest.fixture
def populated_building(building, nails_company, openai_company):
    building[1]=nails_company
    building[2]=openai_company
    yield building

@pytest.fixture
def parametrised_building():
    def _building(a,b):
        return Building(a,b)
    return _building