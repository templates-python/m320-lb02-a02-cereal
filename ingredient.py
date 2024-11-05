""" Provides the Ingredient class for the ingredients of the cereals """
from abc import ABC, abstractmethod


class Ingredient(ABC):
    """
    the ingredients for our cereals

    Attributes
    ----------
    name : str
        Name of the ingredient
    price : float
        Price of the ingredient
    """


    def __init__(self, name, price ):
        """
        Initializes the parameters
        :param name: Name of the ingredient
        :param price: Price of the ingredient
        """
        self.name = name
        self.price = price

    @property
    def name(self):
        """ Get the name of the ingredient """
        return self._name

    @name.setter
    def name(self, value):
        """ Set the name of the ingredient """
        self._name = value

    @property
    def price(self):
        """ Get the price of the ingredient """
        return self._price

    @price.setter
    def price(self, value):
        """ Set the price of the ingredient """
        if value is None or value <= 0.00:
            raise ValueError
        self._price = value

    @abstractmethod
    def __str__(self):
        """ Return the string representation of the object """
        pass