from itertools import chain, combinations, islice
from typing import Iterable, List

import networkx as nx
import numpy as np
from networkx.algorithms.approximation import max_clique

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.file_parser import Client
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class MaxClique(BaseSolver):
    def _solve(self, problem: Problem):
        max_clique = self._get_max_cliques(problem.clients)
        liked_ingredients = {
            chain.from_iterable((client.liked_ingredients for client in max_clique))
        }
        liked_ingredients = set()
        for client in max_clique:
            liked_ingredients.update(client.liked_ingredients)
        return Solution(pizza=Pizza(ingredients=liked_ingredients))

    def _get_max_cliques(self, clients: Iterable[Client]) -> List[List]:
        """Get the max clique (fully connected nodes) where nodes
        represent the clients. The edges indicate if a client can eat
        the same pizza as another client. If you find a clique, it means
        that all clients in the clique can eat the same pizza.

        Args:
            clients (Iterable[Client]): Clients of the problem.

        Returns:
            [List]: A list of clients that form a clique, meaning they can all
            eat the same pizza.
        """
        graph = self._get_graph(clients=clients)
        max_clique_ = max_clique(graph)
        return max_clique_

    def _get_graph(self, clients: Iterable[Client]) -> nx.Graph:
        """Return a graph with nodes as clients and edges if two clients can eat
        the same pizza. Meaning that there are no disliked items of client1 in the
        liked items of client2 and vice versa.

        Args:
            clients (Iterable[Client]): Clients of the problem.

        Returns:
            [nx.Graph]: a graph containing clients as nodes and edges between clients
            that can share the same pizza.
        """
        graph = nx.Graph()
        for client1, client2 in combinations(clients, 2):
            if not (client1.disliked_ingredients & client2.liked_ingredients) and not (
                client2.disliked_ingredients & client1.liked_ingredients
            ):
                graph.add_edge(client1, client2)
        return graph
