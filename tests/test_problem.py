from ..problem import Problem
from unittest.mock import Mock


def test_problem():
    clients = [Mock(), Mock()]
    problem = Problem(clients=clients)
