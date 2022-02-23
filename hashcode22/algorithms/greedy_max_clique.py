import numpy as np

import networkit as nk

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution
from hashcode22.algorithms.max_clique import MaxClique


class GreedyMaxClique(BaseSolver):
    def __init__(self, reduced_problem_size=100):
        self._reduced_problem_size = reduced_problem_size

    def _reduce_problem(self, problem: Problem, selection_method="random"):
        if self._reduced_problem_size >= problem.n_clients:
            return problem.clients
        if selection_method == "random":
            reduced_clients = np.random.choice(
                list(problem.clients), size=self._reduced_problem_size, replace=False
            )
        if selection_method == "sorted":  # sort by degree
            pass
            # ... sort nodes by degree, TODO
        return reduced_clients

    def _is_client_id_in_clique(
        self, G: nk.Graph, client_id: int, client_ids_in_clique: set
    ) -> bool:
        for client_id_in_clique in client_ids_in_clique:
            if not G.hasEdge(client_id, client_id_in_clique):
                return False
        return True

    def grow_clique(
        self, G: nk.Graph, client_ids_in_clique: set, client_ids_outside_clique: set
    ) -> set:
        for client_id in client_ids_outside_clique:
            if self._is_client_id_in_clique(G, client_id, client_ids_in_clique):
                client_ids_in_clique.add(client_id)
        return client_ids_in_clique

    def get_reduced_clique(self, problem: Problem):
        reduced_clients = self._reduce_problem(problem)
        G_reduced = MaxClique()._get_graph(reduced_clients, problem.n_clients)
        reduced_clique = set(MaxClique()._get_max_clique(G_reduced))
        return reduced_clique

    def get_outside_clique(self, problem: Problem, clique: set):
        all_client_ids = set(client.customer_id for client in problem.clients)
        outside_clique = all_client_ids - clique
        return outside_clique

    def _solve(self, problem: Problem):
        G = MaxClique()._get_graph(problem.clients, problem.n_clients)
        reduced_clique = self.get_reduced_clique(problem)
        outside_clique = self.get_outside_clique(problem, reduced_clique)
        max_clique = self.grow_clique(G, reduced_clique, outside_clique)

        liked_ingredients = set()
        client_dict = {client.customer_id: client for client in problem.clients}
        for client_id in max_clique:
            liked_ingredients.update(client_dict[client_id].liked_ingredients)
        return Solution(pizza=Pizza(ingredients=liked_ingredients))
