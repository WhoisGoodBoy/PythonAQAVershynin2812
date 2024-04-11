from lesson17.cat import Cat
import pytest
class TestCat:
    def setup_class(self):
        print('I`m setup class function')
    def setup(self):
        self.cat = Cat('Porphyriy', 'persian', 'fluffy', 4)


    @pytest.mark.regression
    def test_check_growing(self):
        self.cat.grow()
        assert self.cat.age == 5

    def test_check_haircut(self):
        porphyriy = Cat('Porphyriy', 'persian', 'fluffy', 4)
        porphyriy.groom('middle')
        assert porphyriy.haircut == 'middle'

    def teardown(self):
        print('I`m teardown function')

    def teardown_class(self):
        print('I`m teardown class function')