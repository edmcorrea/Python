from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first_ingred = Ingredient("ovo")
    second_ingred = Ingredient("ovo")
    third_ingred = Ingredient("frango")

    assert second_ingred.name == "ovo"
    assert third_ingred.name == "frango"
    assert hash(first_ingred) == hash(second_ingred)
    assert first_ingred == second_ingred
    assert hash(first_ingred) != hash(third_ingred)
    assert first_ingred != third_ingred
    assert second_ingred != third_ingred
    assert repr(third_ingred) == "Ingredient('frango')"

    assert first_ingred.restrictions == {Restriction.ANIMAL_DERIVED}

    assert third_ingred.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    