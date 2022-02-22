from itertools import chain, combinations, islice
from typing import Iterable, List
import numpy as np

import networkit as nk

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.file_parser import Client
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution
from hashcode22.algorithms.max_clique import MaxClique


class GreedyMaxClique(BaseSolver):
    def __init__(self, reduced_problem_size=100):
        self._reduced_problem_size = reduced_problem_size

    def _reduce_problem(self, problem, selection_method = 'random'):
        if self._reduced_problem_size >= problem.n_clients:
            return problem.clients
        if selection_method == 'random':
            reduced_clients = np.random.choice(list(problem.clients), size=self._reduced_problem_size, replace=False)
        if selection_method == 'sorted':    # sort by degree
            pass
            # ... sort nodes by degree, TODO
        return reduced_clients

    def _is_client_id_in_clique(self, client_id: int, client_ids_in_clique: set) -> bool:
        for client_id_in_clique in client_ids_in_clique:
            if not self.G.hasEdge(client_id, client_id_in_clique):
                return False
        return True

    def _grow_clique(self, client_ids_in_clique: set, client_ids_outside_clique: set) -> set:
        for client_id in client_ids_outside_clique:
            if self._is_client_id_in_clique(client_id, client_ids_in_clique):
                client_ids_in_clique.add(client_id)
        return client_ids_in_clique


    def _solve(self, problem: Problem):
        self.G = MaxClique()._get_graph(problem.clients, problem.n_clients)
        client_dict = {client.customer_id:client for client in problem.clients}
        self.n_clients = problem.n_clients
        all_client_ids = set(client_dict.keys())
        reduced_clients = self._reduce_problem(problem)
        G_reduced = MaxClique()._get_graph(reduced_clients, problem.n_clients)
        client_ids_in_clique = set(MaxClique()._get_max_clique(G_reduced))
        client_ids_outside_clique = all_client_ids - client_ids_in_clique
        max_clique = self._grow_clique(client_ids_in_clique, client_ids_outside_clique)

        liked_ingredients = set()
        for client_id in max_clique:
            liked_ingredients.update(client_dict[client_id].liked_ingredients)
        return Solution(pizza=Pizza(ingredients=liked_ingredients))
