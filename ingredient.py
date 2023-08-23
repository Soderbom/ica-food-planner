class Ingredient:
    def __init__(self, id, name, quantity, unit):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit if self.unit else ''} {self.name}"
