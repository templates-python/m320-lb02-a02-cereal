""" Provides the Grain class for the grains of the cereals """
from ingredient import Ingredient


class Grain(Ingredient):
    """
    a type of grain as ingredient of a cereal

    Attributes
    ----------
    allergen : str
        the allergen of this grain
    """

    def __init__(self, name, price, allergen=''):
        """ Creates a new grain with the given name, price and allergen """
        super().__init__(name, price)
        self.allergen = allergen

    def __str__(self):
        """ Returns a string representation of this grain """
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
