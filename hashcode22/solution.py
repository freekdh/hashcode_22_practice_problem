from dataclasses import dataclass

@dataclass
class Solution:
    pizza: str

    @property
    def n_ingredients(self):
        return len(self.pizza.ingredients)

    @property
    def ingredients(self):
        return self.pizza.ingredients