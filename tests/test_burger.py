import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    # создать булку для бургера
    def test_create_buns_to_burger(self):
        burger = Burger()
        bun = Bun('Name_bun', 200.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    # добавить ингредиенты в бургер
    def test_add_ingredient_to_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 888
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 888
        assert burger.ingredients[0].get_name() == 'Name_bun'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING



    # получить стоимость готового бургера с ингредиентами
    def test_get_price_to_burger(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.add_ingredient(database.available_ingredients()[3])
        assert burger.get_price() == 500.0

    # получить чек на бургер
    def test_get_receipt_to_burger(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[2])
        burger.add_ingredient(database.available_ingredients()[4])
        expected_receipt = "(==== white bun ====)\n"\
                           "= sauce chili sauce =\n"\
                           "= filling dinosaur =\n"\
                           "(==== white bun ====)\n\n"\
                           "Price: 900"
        assert expected_receipt == burger.get_receipt()

        