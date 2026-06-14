from optimal_stopping import Selector


def main():
    s = Selector()
    outcomes = [s.run() for _ in range(100)]
    wins = len([outcome.is_best for outcome in outcomes if outcome.is_best]) / len(
        outcomes
    )
    print(wins)


if __name__ == "__main__":
    main()
