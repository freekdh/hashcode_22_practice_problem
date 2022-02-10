from file_parser import FileParser
from problem import Problem

from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from hashcode22.algorithms.genetic_algorithm import GeneticAlgorithm
from hashcode22.algorithms.max_clique import MaxClique
from hashcode22.output_writer import OutputWriter

problem_paths = [
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


def get_problems(problem_paths):
    for problem_path in problem_paths:
        file_parser = FileParser()
        clients = file_parser.parse(f"data/{problem_path}")
        yield Problem(clients=clients)


if __name__ == "__main__":
    problems = list(get_problems(problem_paths=problem_paths))

    output_writer = OutputWriter()
    for i, problem in enumerate(problems):
        print(f"solving problem {i}")
        if len(problem.clients) < 50:
            print("using Brute Force")
            algorithm = BruteForceAlgorithm()
        else:
            print("using Genetic Algorithm")
            algorithm = GeneticAlgorithm(num_generations=1000)
        solution = algorithm.solve(problem)

        print(f"f: = {algorithm.objective_function_pizza(solution.pizza)}")
        output_writer.write(solution, f"./problem_{i}.txt")
