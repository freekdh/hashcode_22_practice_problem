from file_parser import FileParser
from problem import Problem

from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from hashcode22.algorithms.genetic_algorithm import GeneticAlgorithm
from hashcode22.algorithms.max_clique import MaxClique
from hashcode22.output_writer import OutputWriter

problems = [
    "a_an_example.in.txt",
    "b_basic.in.txt",
    "c_coarse.in.txt",
    "d_difficult.in.txt",
    "e_elaborate.in.txt",
]

algorithms = [
    BruteForceAlgorithm(),
    GeneticAlgorithm(),
    MaxClique(),
    MaxClique(heuristic=True),
]

if __name__ == "__main__":
    index = 2
    file_parser = FileParser()
    clients = file_parser.parse(f"data/{problems[index]}")
    problem = Problem(clients=clients)

    for algorithm in algorithms:
        solution = algorithm.solve(problem=problem)

        print(
            f"algorithm {algorithm} f: = {algorithm.objective_function_pizza(pizza=solution.pizza)}"
        )
