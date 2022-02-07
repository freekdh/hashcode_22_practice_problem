from pytest import fixture
from ..file_parser import FileParser


@fixture
def example_input_file():
    return "data/a_an_example.in.txt"


@fixture
def file_parser():
    return FileParser()


def test_parse(file_parser, example_input_file):
    clients = set(file_parser.parse(example_input_file))
    assert len(clients) == 3

    liked = {"basil"}
    disliked = {"pineapple"}

    for client in clients:
        if (
            client.liked_ingredients == liked
            and client.disliked_ingredients == disliked
        ):
            found = True
            break

    assert found
