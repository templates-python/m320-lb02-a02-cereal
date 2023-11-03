from abc import ABC

from ingredient import Ingredient


class Grain(Ingredient, ABC):
    """
    a type of grain as ingredient of a cereal
    """
    def __init__(self, name, price, allergen=''):
        self.name = name
        self.price = price
        self.allergen = allergen

    def __str__(self):
        return f"Grain(name='{self.name}', price={self.price}, allergen='{self.allergen}')"

    @property
    def allergen(self):
        """
        get the allergen of this grain
        """
        return self._allergen

    @allergen.setter
    def allergen(self, value):
        """
        set the allergen of this grain
        """
        self._allergen = value