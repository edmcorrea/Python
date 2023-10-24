import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        new_menu = []
        for dish_elem in self.menu_data.dishes:
            dish = {
                "dish_name": dish_elem.name,
                "ingredients": dish_elem.get_ingredients(),
                "price": dish_elem.price,
                "restrictions": dish_elem.get_restrictions(),
            }
            if restriction is not None and restriction in dish["restrictions"]:
                continue
            new_menu.append(dish)

        return pd.DataFrame(new_menu)
