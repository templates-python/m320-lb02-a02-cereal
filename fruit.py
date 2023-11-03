from abc import ABC

from ingredient import Ingredient


class Fruit(Ingredient, ABC):
    """
    a fruit as ingredient of a cereal
    """

    def __init__(self, name, price, origin):
        self.name = name
        self.price = price
        self.origin = origin

    def __str__(self):
        return f"Fruit(name='{self.name}', price={self.price}, origin='{self.origin}')"

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if value is None or value == '':
            raise ValueError
        self._origin = value