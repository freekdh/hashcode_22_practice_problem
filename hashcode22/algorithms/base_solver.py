from typing import List

import numpy as np

from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem


class BaseSolver:
    def __init__(self):
        pass

    def solve(self, problem: Problem):
        # Prepare the objective function
        ingredients = list(problem.get_ingredients())
        self._index_to_ingredient = {
            index: ingredient for index, ingredient in enumerate(ingredients)
        }
        self._ingredient_to_index = {
            value: key for key, value in self._index_to_ingredient.items()
        }

        self._index_to_client = {
            index: client for index, client in enumerate(problem.clients)
        }
        self._client_to_index = {
            value: key for key, value in self._index_to_client.items()
        }

        self._L_matrix = self._get_L_matrix(
            problem, self._ingredient_to_index, self._client_to_index
        )
        self._n_total_like = np.array(
            [
                len(client.liked_ingredients)
                for index, client in self._index_to_client.items()
            ]
        )
        self._D_matrix = self._get_D_matrix(
            problem, self._ingredient_to_index, self._client_to_index
        )

        return self._solve(problem)

    def _get_L_matrix(self, problem, ingredient_to_index, client_to_index):
        l_matrix = np.zeros((len(problem.clients), len(problem.get_ingredients())))
        for client in problem.clients:
            for ingredient in client.liked_ingredients:
                l_matrix[client_to_index[client]][ingredient_to_index[ingredient]] = 1
        return l_matrix

    def _get_D_matrix(self, problem, ingredient_to_index, client_to_index):
        d_matrix = np.zeros((len(problem.clients), len(problem.get_ingredients())))
        for client in problem.clients:
            for ingredient in client.disliked_ingredients:
                d_matrix[client_to_index[client]][ingredient_to_index[ingredient]] = 1
        return d_matrix

    def objective_function_array(self, solution: List):
        """Compute the objective function of a pizza

        Args:
            pizza (Pizza): [description]
        """
        l_vec = np.array(
            np.dot(self._L_matrix, solution) == self._n_total_like, dtype=int
        )
        d_vec = np.array(np.dot(self._D_matrix, solution) == 0, dtype=int)
        return np.dot(l_vec.T, d_vec)

    def objective_function_pizza(self, pizza: Pizza):
        """Compute the objective function of a pizza

        Args:
            pizza (Pizza): [description]
        """
        l_vec = np.array(
            np.dot(self._L_matrix, solution) == self._n_total_like, dtype=int
        )
        d_vec = np.array(np.dot(self._D_matrix, solution) == 0, dtype=int)
        return np.dot(l_vec.T, d_vec)
