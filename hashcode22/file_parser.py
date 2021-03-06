from dataclasses import dataclass
from itertools import tee
from typing import Iterable

from hashcode22.objects.client import Client


class FileParser:
    def __init__(self):
        pass

    def parse(self, file_path: str) -> Iterable[Client]:
        with open(file_path) as file:
            n_customers = int(next(file).strip())
            for customer_id, (
                liked_ingredients_line,
                disliked_ingredients_line,
            ) in enumerate(zip(file, file)):
                liked_ingredients_line = liked_ingredients_line.strip().split(" ")
                disliked_ingredients_line = disliked_ingredients_line.strip().split(" ")

                liked_ingredients = set(liked_ingredients_line[1:])
                disliked_ingredients = set(disliked_ingredients_line[1:])

                yield Client(
                    customer_id=customer_id,
                    liked_ingredients=liked_ingredients,
                    disliked_ingredients=disliked_ingredients,
                )
