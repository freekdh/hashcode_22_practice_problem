from http import client
from itertools import chain
from multiprocessing.connection import Client
from typing import Iterable
from collections import defaultdict

class Problem:
    def __init__(self, clients: Iterable[Client]):
        self.clients = set(clients)
        self.n_clients = len(self.clients)
        self.ingredients_disliked_dict = self.get_ingredients_disliked_dict()

    def get_ingredients_disliked_dict(self):
        """For each ingredient, generate the set of all clients that dislike it."""
        ingredients_disliked_dict = defaultdict(set)
        for client in self.clients:
            for disliked_ingredient in client.disliked_ingredients:
                ingredients_disliked_dict[disliked_ingredient].add(client.customer_id)
        return ingredients_disliked_dict

    def get_ingredients(self):
        ingredients = set()
        for client in self.clients:
            ingredients.update(set(client.liked_ingredients))
            ingredients.update(set(client.disliked_ingredients))
        return ingredients

    def get_score(self, pizza: "Pizza"):
        score = 0
        for client in self.clients:
            if client.will_eat_pizza(pizza):
                score += 1
        return score
