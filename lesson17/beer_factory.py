from lesson17.factories.stout_factory import StoutFactory
from lesson17.factories.lager_factory import LagerFactory


class AbstractBeerFactory:
    @staticmethod
    def get_factory(beer_type):
        if beer_type == 'lager':
            return LagerFactory()
        elif beer_type == 'stout':
            return StoutFactory()

lager_factory = AbstractBeerFactory.get_factory('lager')
bottle_of_ale = lager_factory.brew_beer('ale')
print(bottle_of_ale)
