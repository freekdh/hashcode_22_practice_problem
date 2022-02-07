from hashcode22.algorithms.brute_force import BruteForceAlgorithm
from file_parser import FileParser
from hashcode22.output_writer import OutputWriter
from problem import Problem


def main(problem):
    solution = BruteForceAlgorithm().solve(problem=problem)
    OutputWriter().write(solution, "/mnt/c/Users/freek/git/HashCode22/test.txt")


if __name__ == "__main__":
    input_file = "data/toy_example.txt"
    file_parser = FileParser()
    clients = file_parser.parse(input_file)
    problem = Problem(clients=clients)
    main(problem=problem)
