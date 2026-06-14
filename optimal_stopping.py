from multiprocessing.resource_sharer import stop
import random

def generate_values(n: int = 100) -> list[float]:
    return [random.random() for _ in range(n)]


class Selector:

    def __init__(self, stopping: float = 0.37):
        self.stopping = stopping
        self.reviewed = []

    def run(self):
        numbers = generate_values()
        print(f"{numbers=}")
        stop_point = round(len(numbers) * self.stopping)
        print(f"{stop_point=}")
        best_yet = max(numbers[:stop_point + 1])
        print(f"{best_yet=}")
        for number in numbers[stop_point:]:
            if number > best_yet:
                return number
        else:
            return number
