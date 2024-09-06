class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def clear(self):
        self.items = []
