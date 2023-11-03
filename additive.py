from abc import ABC

from ingredient import Ingredient


class Additive(Ingredient, ABC):
    """
    an additive (sugar, color, ...) for a cereal
    """

    def __init__(self, name, price, origin, allergen=''):
        self.name = name
        self.price = price
        self.origin = origin
        self.allergen = allergen

    def __str__(self):
        return f"Additive(name='{self.name}', price={self.price}, allergen='{self.allergen}', origin='{self.origin}')"

    @property
    def origin(self):
        """
        get the origin country of the additive
        """
        return self._origin

    @origin.setter
    def origin(self, value):
        """
        set the origin country of the additive
        """
        if value is None or value == '':
            raise ValueError
        self._origin = value

    @property
    def allergen(self):
        """
        get the allergen of this additive
        """
        return self._allergen

    @allergen.setter
    def allergen(self, value):
        """
        set the allergen of this additive
        """
        self._allergen = value