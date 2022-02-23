import numpy as np

import networkit as nk

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution
from hashcode22.algorithms.max_clique import MaxClique
from hashcode22.algorithms.greedy_max_clique import GreedyMaxClique


class LocalSearch(BaseSolver):
    def __init__(self, num_iterations=1000):
        self._num_iterations = num_iterations

    def local_search_step(self, G: nk.Graph, problem: Problem, clique: set):
        outside_clique = GreedyMaxClique().get_outside_clique(problem, clique)
        random_client = np.random.choice(tuple(clique)) # Choose client inside clique
        temp_clique = clique - {random_client}    # remove chosen client from clique
        temp_clique = GreedyMaxClique().grow_clique(G, temp_clique, outside_clique)
        return temp_clique

    def _solve(self, problem: Problem):
        G = MaxClique()._get_graph(problem.clients, problem.n_clients)
        reduced_clique = GreedyMaxClique().get_reduced_clique(problem)
        outside_clique = GreedyMaxClique().get_outside_clique(problem, reduced_clique)
        max_clique = GreedyMaxClique().grow_clique(G, reduced_clique, outside_clique)
        best_solution = len(max_clique)

        for i in range(self._num_iterations):
            temp_clique = self.local_search_step(G, problem, max_clique)
            temp_solution = len(temp_clique)
            if temp_solution >= best_solution:
                print(f"temp solution local search = {temp_solution}, iteration {i}/{self._num_iterations}")
                best_solution = temp_solution
                max_clique = temp_clique

        liked_ingredients = set()
        client_dict = {client.customer_id: client for client in problem.clients}
        for client_id in max_clique:
            liked_ingredients.update(client_dict[client_id].liked_ingredients)
        return Solution(pizza=Pizza(ingredients=liked_ingredients))

