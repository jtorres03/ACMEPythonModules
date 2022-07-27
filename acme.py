"""not sure why but here you go"""
import random


class Product:

    """ Constructor method"""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999+1)

    def stealability(self):
        """Is it stealable?"""
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        if 0.5 <= ratio < 1.0:
            return "Kinda stealable."
        return "Very steaalable!"

    def explode(self):
        """Will it explode"""
        bomb = self.flammability * self.weight
        if bomb < 10:
            return '...fizzle'
        if 10 <= bomb < 50:
            return "...boom!"
        return '...BABOOM!!'


class BoxingGlove(Product):
    """Boxing glove class starts"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """punch will hurt or wont"""
        if self.weight < 5:
            return "That tickles"
        if 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
