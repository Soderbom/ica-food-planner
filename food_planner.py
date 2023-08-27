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

    def print_shopping_list(self):
        with open("shopping_list.txt", "w") as f:
            f.write("Shopping List\n")
            for ingredient in self.shopping_list.values():
                f.write(f"{ingredient}\n")

    def print_recipes(self):
        with open("weekly_recipes.txt", "w") as f:
            for recipe in self.meals:
                f.write(f"{recipe.title}\n")
                f.write(f"{recipe.summary}\n\n")
                f.write("Ingredients:\n")
                for ingredient in recipe.ingredients.values():
                    f.write(f"{ingredient}\n")
                f.write("\n\n")
                f.write("Cooking steps:\n")
                for i, step in enumerate(recipe.cooking_steps):
                    f.write(f"{i+1:3}. {step}\n")
                f.write("-"*10 + "\n\n")


if __name__ == "__main__":
    fp = FoodPlanner(2)
    fp.new_week()
    fp.new_shopping_list()
    fp.print_shopping_list()
    fp.print_recipes()
