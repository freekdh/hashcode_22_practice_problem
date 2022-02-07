from hashcode22.file_parser import FileParser
from hashcode22.problem import Problem
from pytest import fixture


@fixture(scope="session")
def toy_problem():
    clients = FileParser().parse(file_path="data/toy_example.txt")
    return Problem(clients=clients)
