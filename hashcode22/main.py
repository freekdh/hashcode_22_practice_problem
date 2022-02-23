from file_parser import FileParser
from problem import Problem

from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from hashcode22.algorithms.genetic_algorithm import GeneticAlgorithm
from hashcode22.algorithms.max_clique import MaxClique
from hashcode22.algorithms.greedy_max_clique import GreedyMaxClique
from hashcode22.algorithms.local_search import LocalSearch
from hashcode22.output_writer import OutputWriter

problems = {
    "a": "a_an_example.in.txt",
    "b": "b_basic.in.txt",
    "c": "c_coarse.in.txt",
    "d": "d_difficult.in.txt",
    "e": "e_elaborate.in.txt",
}

algorithms = {
    # 'brute_force': BruteForceAlgorithm(),
    # "genetic": GeneticAlgorithm(),
    # 'max_clique': MaxClique()
    # "greedy_max_clique": GreedyMaxClique(),
    "local_search": LocalSearch(),
}


def get_problems(problem_paths):
    for problem_path in problem_paths:
        file_parser = FileParser()
        clients = file_parser.parse(f"data/{problem_path}")
        yield Problem(clients=clients)


if __name__ == "__main__":
    output_writer = OutputWriter()
    for problem_ix in ["e"]:
        for i in range(1):
            print(f"\nSolving problem {problem_ix}")
            file_parser = FileParser()
            file_path = f"data/{problems[problem_ix]}"
            clients = file_parser.parse(file_path)
            problem = Problem(clients=clients)

            for algorithm in algorithms:
                solution = algorithms[algorithm].solve(problem=problem)

                print(
                    f"algorithm {algorithm} f: = {algorithms[algorithm].objective_function_pizza(pizza=solution.pizza)}"
                )
                # output_writer.write(solution, f"./problem_{i}.txt")
