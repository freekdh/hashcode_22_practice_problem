from http import client
from itertools import chain
from multiprocessing.connection import Client
from typing import Iterable


class Problem:
    def __init__(self, clients: Iterable[Client]):
        self.clients = set(clients)
        self.n_clients = len(self.clients)

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
