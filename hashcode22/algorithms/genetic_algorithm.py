import numpy as np
import pygad
from scipy import sparse

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class GeneticAlgorithm(BaseSolver):
    def _solve(self, problem: Problem):
        def fitness_func(solution, solution_idx):
            return self.objective_function_array(solution)

        ga_instance = pygad.GA(
            num_generations=200,
            gene_space=[0, 1],
            num_parents_mating=4,
            fitness_func=fitness_func,
            sol_per_pop=8,
            num_genes=len(list(problem.get_ingredients())),
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
                ingredients_on_pizza.add(self._index_to_ingredient[ingredient_index])

        return Solution(pizza=Pizza(ingredients=ingredients_on_pizza))
