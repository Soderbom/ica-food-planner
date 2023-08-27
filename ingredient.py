class Ingredient:
    def __init__(self, id, name, quantity, unit):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity:5} {self.unit if self.unit else '':4} {self.name}"

    def __add__(self, other):
        # TODO Check unit
        return self.quantity + other.quantity


if __name__ == "__main__":
    a = Ingredient(0, "a", 1, "g")
    b = Ingredient(0, "a", 3, "g")

    assert a + b == 4
