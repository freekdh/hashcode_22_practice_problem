

from hashcode22.solution import Solution
from hashcode22.algorithms.brute_force import Pizza

class SolutionFileParser:
    def __init__(self):
        pass

    def parse(self, file_path: str):
        with open(file_path, "r") as file:
            solution_list = next(file).strip().split(" ")
            solution_list[0]
            solution = Solution(pizza=Pizza(ingredients=set(solution_list[1:])))
        return solution