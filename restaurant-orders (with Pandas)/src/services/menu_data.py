import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.menu_data(source_path)

    def menu_data(self, source_path):
        dishes = {}
        with open(source_path, "r") as file:
            rows = csv.DictReader(file)
            for row in rows:
                row_dish = row["dish"]
                
                dish = dishes.get(row_dish)
                if dish is None:
                    dish = Dish(row_dish, float(row["price"]))
                    dishes[row_dish] = dish
                ingred = Ingredient(row["ingredient"])
                amount = int(row["recipe_amount"])
                dish.add_ingredient_dependency(ingred, amount)
        return set(dishes.values())
