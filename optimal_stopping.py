import random

def generate_values(n: int = 100) -> list[float]:
    return [random.random() for _ in range(n)]