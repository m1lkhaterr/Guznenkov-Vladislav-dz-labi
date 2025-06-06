class Recipe:
    def __init__(self, *args):
        self.recipe = []
        if args:
            for i in args:
                self.recipe.append(i)

    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        self.recipe.remove(ing)

    def get_ingredients(self):
        t_recipe = tuple(self.recipe)
        return t_recipe

    def __len__(self):
        return len(self.recipe)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)
assert len(recipe) == 3
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient)
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure')
assert str(i4) == "Масло: 100, гр" , "метод __str__ вернул неверное значение"
i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4