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
    def __init__(self, stopping: float = 0.37, verbose: bool = False):
        self.stopping = stopping
        self.verbose = verbose
        self.reviewed = []

    def run(self, n: int = 100) -> Outcome:
        number_set = generate_values(n=n)
        if self.verbose:
            print(f"Best available: {number_set.best}.")

        stop_point = round(number=number_set.length * self.stopping)
        best_yet = max(number_set.numbers[: stop_point + 1])
        if self.verbose:
            print(f"Best after {stop_point}: {best_yet}.")

        for number in number_set.numbers[stop_point:]:
            if number > best_yet:
                if self.verbose:
                    print(f"Selecting: {number}")
                return Outcome(
                    selected=number,
                    best=number_set.best,
                    is_best=number == number_set.best,
                )
        else:
            print(f"Selecting final number: {number}")
            return Outcome(
                selected=number, best=number_set.best, is_best=number == number_set.best
            )
