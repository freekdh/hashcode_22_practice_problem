from hashcode22.algorithms.pizza import Pizza
from hashcode22.problem import Problem
import numpy as np
from copy import deepcopy
from hashcode22.solution import Solution
from simanneal import Annealer


class Annealing:
    def __init__(self):
        pass

    def solve(self, problem: Problem):
        x0 = Pizza(ingredients=set())

        class TSA(Annealer):
            def __init__(self, problem, initial_state=None, load_state=None):
                super().__init__(initial_state, load_state)
                self.problem = problem
                self.Tmin = 0.01
                self.Tmax = 2

            def move(self):
                new_state = deepcopy(self.state)
                if np.random.uniform() <= 0.5:
                    # add an element
                    random_ingredient = np.random.choice(list(self.problem.get_ingredients()))
                    new_state.ingredients.add(random_ingredient)
                else:
                    # remove an element
                    try:
                        el = np.random.choice(new_state.ingredients)
                        new_state.ingredients.remote(el)
                    except:
                        pass
                self.state = new_state
                
            def energy(self):
                return -1*self.problem.get_score(self.state)

        it, mil = TSA(problem=problem, initial_state=x0).anneal()
        return Solution(pizza=it)
