import requests
import SECRET
import sys
from recipe import Recipe


encoding = sys.stdin.encoding

USERNAME = SECRET.USERNAME
PASS = SECRET.PASS
url = "https://handla.api.ica.se/api"


units = {
        "krm": 1,
        "tsk": 5,
        "msk": 15,
    }


def make_get_request(path, auth_token):
    return requests.get(
                f"{url}/{path}",
                headers={"AuthenticationTicket": auth_token}
            )


def authenticate(username=USERNAME, password=PASS):
    res = requests.get(f"{url}/login", auth=(USERNAME, PASS))
    return res.headers["AuthenticationTicket"]


def get_random_recipes(auth_token, number_of_recipies=1):
    res = make_get_request(
            f"recipes/random?numberofrecipes={number_of_recipies}",
            auth_token
        )
    return res


if __name__ == "__main__":
    auth_token = authenticate()
    res = get_random_recipes(auth_token)
    recipes = res.json()["Recipes"]

    stored_recipes = []
    for recipe in recipes:
        stored_recipes.append(Recipe(recipe))

    for recipe in stored_recipes:
        print(recipe.title)
