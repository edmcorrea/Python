import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    first_dish = Dish('Lasanha', 42.00)
    second_dish = Dish('Massa', 30.50)
    third_dish = Dish('Lasanha', 42.00)

    assert first_dish.name == 'Lasanha'
    assert first_dish.price == 42.00
    assert repr(first_dish) == "Dish('Lasanha', R$42.00)"

    assert first_dish != second_dish
    assert first_dish == third_dish

    assert hash(first_dish) == hash(first_dish)
    assert hash(first_dish) == hash(third_dish)
    assert hash(first_dish) != hash(second_dish)

    first_ingred = Ingredient('massa de lasanha')
    second_ingred = Ingredient('queijo mussarela')
    third_ingred = Ingredient('presunto')

    first_dish.add_ingredient_dependency(first_ingred, 1)
    first_dish.add_ingredient_dependency(second_ingred, 10)
    first_dish.add_ingredient_dependency(third_ingred, 5)

    expected_recipe = {
        first_ingred: 1,
        second_ingred: 10,
        third_ingred: 5
    }

    assert first_dish.recipe == expected_recipe
    assert first_dish.get_ingredients() == expected_recipe.keys()

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT
    }

    with pytest.raises(TypeError, match='Dish price must be float'):
        Dish('Teste', '42.00')

    with pytest.raises(ValueError, match='price must be greater then zero.'):
        Dish('Teste', -42)

    assert first_dish.get_restrictions() == expected_restrictions
