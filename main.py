from optimal_stopping import Selector


def main():
    # create a selector to review 'candidates'
    s = Selector(stopping=0.37)

    # run N experiments
    # reject the first 37% of candidates then choose next candidate that is better than the best yet
    outcomes = [s.run() for _ in range(1000)]

    # review results - how often did we get the best candidate?
    wins = len([outcome.is_best for outcome in outcomes if outcome.is_best]) / len(
        outcomes
    )
    print(f"Win rate: {wins:.2%}")


if __name__ == "__main__":
    main()
