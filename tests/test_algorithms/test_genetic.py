from hashcode22.algorithms.genetic_algorithm import GeneticAlgorithm

from ..fixtures import toy_problem


def test_genetic(toy_problem, tmp_path):
    max_clique = GeneticAlgorithm()
    solution = max_clique.solve(toy_problem)
