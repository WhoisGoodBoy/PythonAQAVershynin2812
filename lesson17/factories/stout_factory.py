from lesson17.factories import BeerFactory, Dry, Milk


class StoutFactory(BeerFactory):
    _beer_type = 'stout'

    def __init__(self):
        self.name = 'Heinikenn'
        self._positions = ['milk', 'dry']

    @property
    def positions(self):
        return self._positions

    def brew_beer(self, name):
        if name == 'milk':
            return Milk()
        elif name == 'dry':
            return Dry()