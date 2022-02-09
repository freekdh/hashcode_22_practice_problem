from dataclasses import dataclass
from itertools import chain, combinations
from typing import Iterable

from hashcode22.objects.pizza import Pizza
from hashcode22.problem import Problem
from hashcode22.solution import Solution


class BruteForceAlgorithm:
    """The brute force algorithm simply explores all possible
    ingredient combinations and chooses the combintation that
    leads to the most clients eating the pizza.
    """

    def solve(self, problem: Problem):
        ingredients = problem.get_ingredients()
        best_score, best_pizza = 0, None
        for consider_ingredients in self._powerset(ingredients):
            pizza = Pizza(ingredients=set(consider_ingredients))
            score = problem.get_score(pizza)
            if score > best_score:
                best_score = score
                best_pizza = pizza
        return Solution(pizza=best_pizza)

    def _powerset(self, iterable: Iterable) -> Iterable:
        """Return the powerset of an iterable

        Args:
            iterable ([Iterable]): Any iterable

        Returns:
            [Iterable]: An iterable over the powerset of the input iterable
        """
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
