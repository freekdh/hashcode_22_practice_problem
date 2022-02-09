from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Client:
    customer_id: int
    liked_ingredients: set
    disliked_ingredients: set

    def __repr__(self):
        return str(self.customer_id)

    def will_eat_pizza(self, pizza):
        if (
            self.liked_ingredients.issubset(pizza.ingredients)
            and not self.disliked_ingredients & pizza.ingredients
        ):
            return True
        else:
            return False
