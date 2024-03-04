import pytest

from lesson15.len_dict_example import Company

@pytest.mark.regression
@pytest.mark.skip(reason='not run yet because of issue 9671')
def test_building_len(building):
    openai = Company('OpenAI', 'artificial intelligence')
    building[1] = openai
    assert len(building) == 1


@pytest.mark.regression
def test_building_len_with_multiple_fixtures(building, nails_company, openai_company):
    building[1]=nails_company
    building[2]=openai_company
    assert len(building)==2


@pytest.mark.regression
def test_building_len_with_complex_fixture(populated_building):
    assert len(populated_building) == 2

@pytest.mark.parametrize(
    'company_name,expected_name,company_industry,expected_industry',[('a', 'a', 'b', 'b'), ('c','c', 'd', 'e')]
)
def test_building_company_parametrised(building, company_name,expected_name,company_industry,expected_industry):
    building[1]=Company(company_name,company_industry)
    assert building[1].name == expected_name
    assert building[1].industry == expected_industry


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason='still issue 6741, but this time we should try to run it', condition=True)
@pytest.mark.parametrize(
    'company,expected_name,expected_industry',
    [(Company('a', 'b'),'a', 'b'),
     (Company('c', 'd'), 'c', 'e')],
    ids=['first case', 'second case']
)
def test_building_company_parametrised2(building, company,expected_name,expected_industry):
    building[1]=company
    assert building[1].name == expected_name
    assert building[1].industry == expected_industry

def test_company_added():
    pass

