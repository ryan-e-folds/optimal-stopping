import random
from pydantic import BaseModel


class NumberSet(BaseModel):
    numbers: list[int]
    best: int
    length: int


class Outcome(BaseModel):
    selected: int
    best: int
    is_best: bool


def generate_values(n: int = 100) -> NumberSet:
    numbers = [random.randint(0, 1_000_000) for _ in range(n)]
    return NumberSet(numbers=numbers, best=max(numbers), length=len(numbers))


class Selector:
    def __init__(self, stopping: float = 0.37):
        self.stopping = stopping
        self.reviewed = []

    def run(self, n: int = 100) -> Outcome:
        number_set = generate_values(n=n)
        stop_point = round(number=number_set.length * self.stopping)
        best_yet = max(number_set.numbers[: stop_point + 1])
        for number in number_set.numbers[stop_point:]:
            if number > best_yet:
                return Outcome(
                    selected=number,
                    best=number_set.best,
                    is_best=number == number_set.best,
                )
        else:
            return Outcome(
                selected=number, best=number_set.best, is_best=number == number_set.best
            )
