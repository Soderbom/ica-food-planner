import requests
from recipe import Recipe
import SECRET


class FoodPlanner:
    def __init__(self, number_of_meals):
        self.number_of_meals = number_of_meals
        self.meals = []
        self.shopping_list = {}
        self.username = SECRET.USERNAME
        self.password = SECRET.PASS
        self.url = "https://handla.api.ica.se/api"
        self.auth_token = self._authenticate()

    def make_get_request(self, path):
        return requests.get(
            f"{self.url}/{path}",
            headers={"AuthenticationTicket": self.auth_token})

    def _authenticate(self):
        res = requests.get(
                f"{self.url}/login",
                auth=(self.username, self.password))
        return res.headers["AuthenticationTicket"]

    def get_random_recipes(self, number_of_recipies=1):
        res = self.make_get_request(
                f"recipes/random?numberofrecipes={number_of_recipies}"
            )
        return res.json()["Recipes"]

    def new_week(self):
        self.meals = [Recipe(recipe)
                      for recipe in self.get_random_recipes(
                          self.number_of_meals)]

    def new_shopping_list(self):
        ingredients = {}
        for recipe in self.meals:
            for id, ingredient in recipe.ingredients.items():
                if ingredients.get(ingredient):
                    ingredients.get(ingredient) + ingredient
                else:
                    ingredients[id] = ingredient
        self.shopping_list = ingredients


if __name__ == "__main__":
    fp = FoodPlanner(2)
    fp.new_week()
    fp.new_shopping_list()
