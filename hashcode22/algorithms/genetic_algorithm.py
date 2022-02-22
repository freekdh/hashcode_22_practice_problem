import numpy as np
import pygad
from scipy import sparse

from hashcode22.algorithms.base_solver import BaseSolver
from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class GeneticAlgorithm(BaseSolver):
    def __init__(
        self,
        num_generations=200,
        num_parents_mating=20,
        sol_per_pop=8,
        parent_selection_type="sss",
        crossover_type="single_point",
        mutation_type="random",
    ):
        self._num_generations = num_generations
        self._num_parents_mating = num_parents_mating
        self._sol_per_pop = sol_per_pop
        self._parent_selection_type = parent_selection_type
        self._crossover_type = crossover_type
        self._mutation_type = mutation_type

    def _solve(self, problem: Problem):
        def fitness_func(solution, solution_idx):
            return self.objective_function_solution_list(solution)

        ga_instance = pygad.GA(
            num_generations=self._num_generations,
            gene_space=[0, 1],
            num_parents_mating=self._num_parents_mating,
            fitness_func=fitness_func,
            sol_per_pop=self._sol_per_pop,
            num_genes=len(list(problem.get_ingredients())),
            parent_selection_type=self._parent_selection_type,
            keep_parents=1,
            crossover_type=self._crossover_type,
            mutation_type=self._mutation_type,
            mutation_percent_genes=10,
            suppress_warnings=True,
        )

        ga_instance.run()

        ga_instance.plot_fitness(save_dir="./plot_fitness")

        best_solution = ga_instance.best_solution()[0]
        ingredients_on_pizza = set()
        for ingredient_index, value in enumerate(best_solution):
            if value:
                ingredients_on_pizza.add(self._index_to_ingredient[ingredient_index])

        return Solution(pizza=Pizza(ingredients=ingredients_on_pizza))
