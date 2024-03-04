from lesson17.factories import BeerFactory, Lager,Ale


class LagerFactory(BeerFactory):
    _beer_type = 'lager'

    def __init__(self):
        self.name = 'Rogan'
        self._positions = ['lager', 'ale']

    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == 'lager':
            return Lager()
        elif name == 'ale':
            return Ale()