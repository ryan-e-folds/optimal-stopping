# Optimal Stopping

A Python implementation of the [optimal stopping problem](https://en.wikipedia.org/wiki/Optimal_stopping) (also known as the Secretary problem), demonstrating how to maximize the probability of selecting the best candidate from a sequence of random values.

## Features

- **Selector**: Core algorithm implementing the optimal stopping strategy
- **Configurable Threshold**: Adjust the stopping percentage to experiment with different strategies
- **Outcome Tracking**: Evaluates whether the selected candidate was indeed the best
- **Batch Experiments**: Run multiple trials to calculate win rates

## Installation

```bash
git clone https://github.com/ryan-e-folds/optimal-stopping.git
```

```
uv sync
```

## Usage

```python
from optimal_stopping import Selector

# Create a selector with the optimal 37% threshold
s = Selector(stopping=0.37)

# Run a single trial with 100 candidates
outcome = s.run(n=100)
print(f"Selected: {outcome.selected}, Best available: {outcome.best}")
print(f"Is best? {outcome.is_best}")

# Run multiple experiments
outcomes = [s.run() for _ in range(1000)]
win_rate = sum(1 for o in outcomes if o.is_best) / len(outcomes)
print(f"Win rate: {win_rate:.2%}")
```

## Running the Demo

```bash
uv run main.py
```

This runs 1000 experiments using the optimal stopping strategy and displays the win rate.

## Example Output

```
Win rate: 37.10%
```

With the 37% rule, you should expect a win rate around 37%, which is significantly better than random selection (1%) and approaches the theoretical optimal of ~37.1%.

## Project Structure

- `optimal_stopping.py`: Core implementation with `Selector` class and supporting models
- `main.py`: Demo script running multiple experiments
- `pyproject.toml`: Project metadata and dependencies

## How It Works

1. **Generate**: Create a random sequence of N candidates
2. **Skip Phase**: Reject the first 37% of candidates, tracking the best seen
3. **Selection Phase**: Review remaining candidates and select the first one better than the best from the skip phase
4. **Evaluate**: Check if the selected candidate was the best overall

## Theoretical Basis

The 37% threshold (1/e ≈ 0.368) is derived from optimal control theory. It minimizes the probability of both:
- Stopping too early (missing the best candidate)
- Stopping too late (passing on the best candidate)