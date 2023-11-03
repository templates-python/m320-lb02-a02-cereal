from abc import ABC, abstractmethod


class Ingredient(ABC):
    """
    the ingredients for our cereals
    """

    @abstractmethod
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None or value <= 0.00:
            raise ValueError
        self._price = value