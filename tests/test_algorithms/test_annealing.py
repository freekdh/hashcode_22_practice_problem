from hashcode22.algorithms.annealing import Annealing

from ..fixtures import toy_problem


def test_sat_solver(toy_problem, tmp_path):
    annealing_solver = Annealing()
    solution = annealing_solver.solve(toy_problem)
