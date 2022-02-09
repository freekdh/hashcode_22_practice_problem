from hashcode22.algorithms.annealing import Annealing
from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from hashcode22.algorithms.max_clique import MaxClique
from file_parser import FileParser
from hashcode22.output_writer import OutputWriter
from problem import Problem

problems = [
    "a_an_example.in.txt",
    "b_basic.in.txt",
    "c_coarse.in.txt",
    "d_difficult.in.txt",
    "e_elaborate.in.txt",
]


if __name__ == "__main__":
    index = 3

    file_parser = FileParser()
    clients = file_parser.parse(f"data/{problems[index]}")
    problem = Problem(clients=clients)
    solution = MaxClique().solve(problem=problem)
    OutputWriter().write(solution, f"solution_{index}.txt")
