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


def test_cereal_with_ingredients(make_cereal):
    assert isinstance(make_cereal, Cereal)
    assert len(make_cereal.ingredients) == 4


def test_ingredient_to_cereal():
    cereal = Cereal('Fastbreak')
    cereal_ingredient = CerealIngredient(cereal, None, 100)
    assert cereal_ingredient.cereal.cereal_name == 'Fastbreak'


def test_calculate_cost(capsys, make_cereal):
    make_cereal.calculate_cost(750)
    output = capsys.readouterr().out
    assert output == 'Cost: 925.50\n'


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