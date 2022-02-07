from itertools import chain, combinations
from typing import Iterable
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
        for ingredients_ in self._powerset(ingredients):
            pizza = self._make_pizza(ingredients)
            score = problem.get_score(pizza)
            if score > 0:
                pass

        return None

    def _make_pizza(self, ingredients: Iterable[set]):
        return Pizza(ingredients=ingredients)

    def _powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
