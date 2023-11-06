from random import random, randint

import pytest

from additive import Additive
from cereal import Cereal
from cereal_ingredient import CerealIngredient
from fruit import Fruit
from grain import Grain


def test_cereal_empty():
    cereal = Cereal('My mampf')
    assert isinstance(cereal, Cereal)
    assert len(cereal.ingredients) == 0
    assert isinstance(type(cereal).cereal_name, property)
    assert isinstance(type(cereal).ingredients, property)


def test_cereal_with_ingredients(make_cereal):
    assert isinstance(make_cereal, Cereal)
    assert len(make_cereal.ingredients) == 4


def test_add_ingredient(make_cereal):
    ingredient = Additive('Sawdust', 0.01, 'SA', 'wood')
    make_cereal.add_ingredient(CerealIngredient(make_cereal, ingredient, 0.1))
    assert len(make_cereal.ingredients) == 5


def test_take_ingredient(make_cereal):
    cereal_ingredient = make_cereal.take_ingredient(2)
    assert cereal_ingredient.ingredient.name == 'Oats'


def test_remove_ingredient(make_cereal):
    make_cereal.remove_ingredient(1)
    assert len(make_cereal.ingredients) == 3
    assert make_cereal.ingredients[1].ingredient.name == 'Oats'


def test_ingredient_to_cereal():
    cereal = Cereal('Fastbreak')
    cereal_ingredient = CerealIngredient(cereal, None, 0.99)
    assert cereal_ingredient.cereal.cereal_name == 'Fastbreak'
    assert isinstance(type(cereal_ingredient).ingredient, property)
    assert isinstance(type(cereal_ingredient).proportion, property)


def test_calculate_cost(capsys, make_cereal):
    amount = randint(500,999)
    cost = make_cereal.calculate_cost(amount)
    assert cost == pytest.approx(amount*1.234)


@pytest.fixture
def make_cereal(make_ingredients):
    return Cereal('Duckula', [
        CerealIngredient(None, make_ingredients[0], 0.15),
        CerealIngredient(None, make_ingredients[1], 0.25),
        CerealIngredient(None, make_ingredients[2], 0.4),
        CerealIngredient(None, make_ingredients[3], 0.20)
    ])


@pytest.fixture()
def make_ingredients():
    ingredient1 = Fruit('Kiwi', 2.75, 'NZ')
    ingredient2 = Fruit('Strawberry', 3.15, 'CH')
    ingredient3 = Grain('Oats', 0.07, 'Gluten')
    ingredient4 = Additive('Sugar', 0.03, 'AU', '')
    return [ingredient1, ingredient2, ingredient3, ingredient4]
