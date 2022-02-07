from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from file_parser import FileParser
from problem import Problem


def main(problem):
    solution = BruteForceAlgorithm().solve(problem=problem)
    print(solution)


if __name__ == "__main__":
    input_file = "data/a_an_example.in.txt"
    file_parser = FileParser()
    clients = file_parser.parse(input_file)
    problem = Problem(clients=clients)
    main(problem=problem)
