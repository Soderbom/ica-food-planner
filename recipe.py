from ingredient import Ingredient
from bs4 import BeautifulSoup


class Recipe:
    def __init__(self, recipe_json):
        self.id = recipe_json["Id"]
        self.title = recipe_json["Title"]
        self.image_url = recipe_json["ImageUrl"]
        self.ingredients = self._parse_ingredients(
                recipe_json["IngredientGroups"]
            )
        self.nutrition_per_portion = recipe_json["NutritionPerPortion"]
        self.cooking_steps = self._parse_cooking_steps(
                recipe_json["CookingSteps"])
        self.cooking_time = recipe_json["CookingTime"]
        self.rating = recipe_json["AverageRating"]
        self.summary = recipe_json["PreambleHTML"]

    def _parse_ingredients(self, ingredients_group):
        ingredients = {}
        for ingredient in ingredients_group[0]["Ingredients"]:
            id = ingredient["IngredientId"]
            name = ingredient["Ingredient"]
            quantity = ingredient["Quantity"]
            unit = ingredient.get("Unit")

            if stored_ingredient := ingredients.get(id):
                if stored_ingredient.unit == unit:
                    stored_ingredient.quantity += quantity
                else:
                    # TODO Convert units
                    pass
            else:
                ingredients[id] = Ingredient(id, name, quantity, unit)

        return ingredients

    def _parse_cooking_steps(self, html_cooking_steps):
        cooking_steps = []
        for step in html_cooking_steps:
            cooking_steps.append(
                BeautifulSoup(step, "html.parser")
                )

        return cooking_steps

    def get_summary(self):
        return self.summary
