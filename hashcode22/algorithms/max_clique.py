from itertools import chain, combinations, islice
from typing import Iterable, List

import networkit as nk

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.file_parser import Client
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class MaxClique(BaseSolver):
    def __init__(self, print_stats=False):
        self._print_stats = print_stats

    def _solve(self, problem: Problem):
        client_dict = {client.customer_id: client for client in problem.clients}
        self.n_clients = problem.n_clients
        G = self._get_graph(problem.clients, problem.n_clients)
        max_clique = self._get_max_clique(G)
        liked_ingredients = set()
        for client_id in max_clique:
            liked_ingredients.update(client_dict[client_id].liked_ingredients)
        return Solution(pizza=Pizza(ingredients=liked_ingredients))

    def _get_max_clique(self, G: nk.Graph) -> List[List]:
        """Get the max clique (fully connected nodes) where nodes
        represent the clients. The edges indicate if a client can eat
        the same pizza as another client. If you find a clique, it means
        that all clients in the clique can eat the same pizza.

        Args:
            graph (nk.Graph): Graph of clients with compatible pizzzas.

        Returns:
            [List]: A list of clients that form a clique, meaning they can all
            eat the same pizza.
        """
        get_max_clique = nk.clique.MaximalCliques(G, maximumOnly=True)
        get_max_clique.run()
        max_clique = get_max_clique.getCliques()[0]

        return max_clique

    def _get_graph(self, clients: Iterable[Client], n_clients: int) -> nk.Graph:
        """Return a graph with nodes as clients and edges if two clients can eat
        the same pizza. Meaning that there are no disliked items of client1 in the
        liked items of client2 and vice versa.

        Args:
            clients (Iterable[Client]): Clients of the problem.
            n_clients (int): Number of clients

        Returns:
            [nk.Graph]: a graph containing clients as nodes and edges between clients
            that can share the same pizza.
        """
        G = nk.Graph(n_clients)
        for client1, client2 in combinations(clients, 2):
            if not (client1.disliked_ingredients & client2.liked_ingredients) and not (
                client2.disliked_ingredients & client1.liked_ingredients
            ):
                G.addEdge(client1.customer_id, client2.customer_id)
        print("Graph built, done!")
        if self._print_stats:
            print("=" * 45)
            nk.overview(G)  # Get statistics on graph
            print("=" * 45)
        return G
