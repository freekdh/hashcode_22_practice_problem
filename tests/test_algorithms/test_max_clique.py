
from hashcode22.algorithms.max_clique import MaxClique
from ..fixtures import toy_problem

def test_max_clique(toy_problem, tmp_path):
    max_clique = MaxClique()
    solution = max_clique.solve(toy_problem)