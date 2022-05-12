from collections import Counter

class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []
        self.all_ingredients = []

    def add_new_order(self, customer, order, day):
        return self.orders.append(
            {"customer": customer, "order": order, "day": day}
        )

    def get_quantities_to_buy(self):
        ingredients_to_buy = []
        self.all_ingredients.extend(self.INGREDIENTS.values())
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
        self.all_ingredients = set(item for sublist in self.all_ingredients for item in sublist)
        for order in self.orders:
            ingredients_to_buy.extend(self.INGREDIENTS[order["order"]])
        ingredients_to_buy = dict(Counter(ingredients_to_buy))
        self.all_ingredients = dict.fromkeys(self.all_ingredients, 0)
        self.all_ingredients.update(ingredients_to_buy)
        return self.all_ingredients