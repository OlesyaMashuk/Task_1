from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

    # получить количество возмодных булок для бургера
    def test_get_quantity_buns(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

    # получить количество возможных соусов для бургера"
    def test_get_quantity_sauces(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3   

    # получить количество возможных ингредиентов для бургера"
    def test_get_quantity_ingredients(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6


    # получить количество возможных начинок для бургера"
    def test_get_quantity_fillings(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_fillings) == 3
