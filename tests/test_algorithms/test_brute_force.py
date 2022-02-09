import filecmp

from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from hashcode22.output_writer import OutputWriter
from hashcode22.solution_file_parser import SolutionFileParser

from ..fixtures import toy_problem


def test_brute_force(toy_problem, tmp_path):
    brute_force = BruteForceAlgorithm()
    solution = brute_force.solve(toy_problem)
    OutputWriter().write(solution, f"{tmp_path}/tmp.txt")

    solution = SolutionFileParser().parse(f"{tmp_path}/tmp.txt")
    n_ingredients = len(solution.ingredients)
    print(solution.ingredients)
    print(n_ingredients)
