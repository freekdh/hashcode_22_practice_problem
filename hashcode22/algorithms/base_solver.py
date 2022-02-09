from typing import List

import numpy as np

from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class BaseSolver:
    """Base Solver Class gives access to objective function of the problem and
    other useful tools for solving the problem.
    """

    def solve(self, problem: Problem) -> Solution:
        """Wrapper function for solving a problem. Here we initialize the creation of
        the L and U matrix used for calculating the objective function.

        Args:
            problem (Problem): A problem to be solved.

        Returns:
            [Solution]: A solution object
        """
        self._initialize_objective_function(problem)
        return self._solve(problem)

    def objective_function_solution_list(self, solution: List):
        """Compute the objective function of a pizza

        Args:
            solution (List): The pizza in the form of a list (using self._index_to_ingredient)
            to indicate which index corresponds to which ingredient.
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
        solution_list = self.pizza_to_solution_list(pizza)
        return self.objective_function_solution_list(solution_list)

    def pizza_to_solution_list(self, pizza: Pizza):
        solution_list = [0] * len(self._ingredient_to_index)
        for ingredient in pizza.ingredients:
            solution_list[self._ingredient_to_index[ingredient]] = 1
        return solution_list

    def solution_list_to_pizza(self, solution_list: List):
        raise NotImplementedError

    def _initialize_objective_function(self, problem: Problem):
        """Prepare the index_to_ingredient, index_to_client and
        the L and D matrix which are used to calculate the objective function.

        Args:
            problem (Problem): The problem to be solved.
        """
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

    def _get_L_matrix(
        self, problem: Problem, ingredient_to_index: dict, client_to_index: dict
    ):
        """The matrix containing a 1 if the client liked the ingredient and 0
        if the client does not.

        Args:
            problem ([Problem]): A problem to be solved.
            ingredient_to_index ([dict]): Ingredients to index mapping
            client_to_index ([dict]): Client to index mapping

        Returns:
            [Numpy.Array()]: Matrix containing what ingredients clients like
        """
        l_matrix = np.zeros((len(problem.clients), len(problem.get_ingredients())))
        for client in problem.clients:
            for ingredient in client.liked_ingredients:
                l_matrix[client_to_index[client]][ingredient_to_index[ingredient]] = 1
        return l_matrix

    def _get_D_matrix(self, problem, ingredient_to_index, client_to_index):
        """The matrix containing a 1 if the client disliked the ingredient and 0
        if the client does not dislike it.

        Args:
            problem ([Problem]): A problem to be solved.
            ingredient_to_index ([dict]): Ingredients to index mapping
            client_to_index ([dict]): Client to index mapping

        Returns:
            [Numpy.Array()]: Matrix containing what ingredients clients disliked
        """
        d_matrix = np.zeros((len(problem.clients), len(problem.get_ingredients())))
        for client in problem.clients:
            for ingredient in client.disliked_ingredients:
                d_matrix[client_to_index[client]][ingredient_to_index[ingredient]] = 1
        return d_matrix
