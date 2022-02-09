from typing import Iterable
from hashcode22.algorithms.pizza import Pizza
from hashcode22.problem import Problem
import networkx as nx
from itertools import combinations
from networkx.algorithms import find_cliques
from hashcode22.solution import Solution
import numpy as np
from hashcode22.file_parser import Client
from itertools import islice

class MaxClique:
    def __init__(self, max_n_clients=50):
        self._max_n_clients = max_n_clients

    def _get_cliques(self, clients: Iterable[Client]):
        clients = list(clients)
        graph = self._get_graph(clients=clients)
        return list(find_cliques(graph))        

    def solve(self, problem: Problem):
        if len(list(problem.clients)) < self._max_n_clients:
            cliques = self._get_cliques(problem.clients)
            max_clique = max(cliques, key=len)
            liked_ingredients, disliked_ingredients = set(), set()
            for client in max_clique:
                liked_ingredients.update(client.liked_ingredients)
            return Solution(pizza=Pizza(ingredients=liked_ingredients))
        else:
            cliques = []
            clients_generator = iter(problem.clients)
            while True:
                sample_clients = list(islice(clients_generator, self._max_n_clients))
                if not sample_clients:
                    break
                for clique in self._get_cliques(sample_clients):
                    cliques.append(clique)
            sorted_cliques = list(reversed(sorted(cliques, key=len)))
            new_clients = []
            for index, clique in enumerate(sorted_cliques):
                liked_ingredients, disliked_ingredients = set(), set()
                for client in clique:
                    liked_ingredients.update(client.liked_ingredients)
                    disliked_ingredients.update(client.disliked_ingredients)
                superclient = Client(customer_id=index, liked_ingredients=liked_ingredients, disliked_ingredients=disliked_ingredients)
                superclient_weight = len(clique)
                new_clients.append((superclient, superclient_weight))

            weighted_graph = self._get_weighted_graph(new_clients)
            breakpoint()

    def _get_graph(self, clients):
        graph = nx.Graph()
        for client1, client2 in combinations(clients, 2):
            if not (client1.disliked_ingredients & client2.liked_ingredients) and not (client2.disliked_ingredients & client1.liked_ingredients):
                graph.add_edge(client1, client2)
        return graph

    def _get_weighted_graph(self, clients_with_weights):
        graph = nx.Graph()
        for (client1, weight1), (client2, weight2) in combinations(clients_with_weights, 2):
            if not (client1.disliked_ingredients & client2.liked_ingredients) and not (client2.disliked_ingredients & client1.liked_ingredients):
                graph.add_edge(client1, client2)
                graph.nodes[client1]["weight"] = weight1
                graph.nodes[client2]["weight"] = weight2 
                print("EDGE!!")
        return graph
