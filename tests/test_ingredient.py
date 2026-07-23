import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

     # получить корректное наименование ингредиента
    def test_get_name_returns_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    # получить корректную стоимость ингредиента
    def test_get_price_returns_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    # получить тип ингредиента (соус)
    def test_get_type_returns_value(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 200)
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE
        

    
   
