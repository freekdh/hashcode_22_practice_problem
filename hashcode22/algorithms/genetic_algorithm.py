import numpy as np
import pygad
from scipy import sparse

from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class GeneticAlgorithm:
    def __init__(self):
        pass

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

    def solve(self, problem: Problem):

        ingredients = list(problem.get_ingredients())

        index_to_ingredient = {
            index: ingredient for index, ingredient in enumerate(ingredients)
        }
        ingredient_to_index = {value: key for key, value in index_to_ingredient.items()}

        index_to_client = {
            index: client for index, client in enumerate(problem.clients)
        }
        client_to_index = {value: key for key, value in index_to_client.items()}

        L_matrix = self._get_L_matrix(problem, ingredient_to_index, client_to_index)
        n_total_like = np.array(
            [len(client.liked_ingredients) for index, client in index_to_client.items()]
        )
        D_matrix = self._get_D_matrix(problem, ingredient_to_index, client_to_index)

        def fitness_func(solution, solution_idx):
            l_vec = np.array(np.dot(L_matrix, solution) == n_total_like, dtype=int)
            d_vec = np.array(np.dot(D_matrix, solution) == 0, dtype=int)
            return np.dot(l_vec.T, d_vec)

        ga_instance = pygad.GA(
            num_generations=200,
            gene_space=[0, 1],
            num_parents_mating=4,
            fitness_func=fitness_func,
            sol_per_pop=8,
            num_genes=len(ingredients),
            parent_selection_type="sss",
            keep_parents=1,
            crossover_type="single_point",
            mutation_type="random",
            mutation_percent_genes=10,
        )

        ga_instance.run()
        best_solution = ga_instance.best_solution()[0]
        ingredients_on_pizza = set()
        for ingredient_index, value in enumerate(best_solution):
            if value:
                ingredients_on_pizza.add(index_to_ingredient[ingredient_index])

        return Solution(pizza=Pizza(ingredients=ingredients_on_pizza))
