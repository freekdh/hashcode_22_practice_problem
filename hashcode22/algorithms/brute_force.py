from itertools import chain, combinations
from typing import Iterable

from hashcode22.solution import Solution
from ..problem import Problem
from dataclasses import dataclass


@dataclass
class Pizza:
    ingredients: set


class BruteForceAlgorithm:
    def __init__(self):
        pass

    def solve(self, problem: Problem):
        ingredients = problem.get_ingredients()
        best_score, best_pizza = 0, None
        for consider_ingredients in self._powerset(ingredients):
            pizza = self._make_pizza(consider_ingredients)
            score = problem.get_score(pizza)
            if score > best_score:
                best_score = score
                best_pizza = pizza
        return Solution(pizza=best_pizza)

    def _make_pizza(self, ingredients: Iterable[set]):
        return Pizza(ingredients=set(ingredients))

    def _powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
