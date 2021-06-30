class InventoryControl:
    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.total_ingredients = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, _costumer, order, _day):
        if order in self.get_available_dishes():
            for ing in self.ingredients[order]:
                self.total_ingredients[ing] = self.total_ingredients.get(
                    ing,
                    0
                ) + 1
        else:
            return False

    def get_quantities_to_buy(self):
        return self.total_ingredients

    def get_available_dishes(self):
        dishes = set()
        for ing in self.minimum_inventory.keys():
            if self.total_ingredients[ing] >= self.minimum_inventory[ing]:
                for p in self.ingredients.keys():
                    if ing in self.ingredients[p]:
                        dishes.add(p)
        h = {p for p in self.ingredients.keys()}
        return h.difference(dishes)
