from ..file_parser import FileParser
from ..problem import Problem
from pytest import fixture


@fixture(scope="session")
def toy_problem():
    clients = FileParser().parse(file_path="data/a_an_example.in.txt")
    return Problem(clients=clients)
