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
        best_score, best_pizza = 0, None
        for ingredients_ in self._powerset(ingredients):
            pizza = self._make_pizza(ingredients_)
            score = problem.get_score(pizza)
            if score > best_score:
                score = best_score
                best_pizza = pizza
        return best_pizza

    def _make_pizza(self, ingredients: Iterable[set]):
        return Pizza(ingredients=ingredients)

    def _powerset(self, iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
