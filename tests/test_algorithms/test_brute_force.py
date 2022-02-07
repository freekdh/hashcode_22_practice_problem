from ...algorithms.brute_force import BruteForceAlgorithm
from ..fixtures import toy_problem


def test_brute_force(toy_problem):
    brute_force = BruteForceAlgorithm()
    problem = brute_force.solve(toy_problem)
