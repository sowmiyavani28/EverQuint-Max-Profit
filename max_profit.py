
from functools import lru_cache

# Building details:
# (Name, Construction Time, Earnings per Operating Time Unit)

BUILDINGS = [
    ("T", 5, 1500),   # Theatre
    ("P", 4, 1000),   # Pub
    ("C", 10, 2000),  # Commercial Park
]


def max_profit(n):
    """
    Calculate maximum earnings for a given time budget.

    Assumptions:
    - Only one building can be constructed at a time.
    - Buildings are constructed sequentially.
    - Earnings start after construction is complete.
    - Each completed building continues earning until time n.
    - A building completed exactly at time n earns zero.
    - Return all unique building combinations achieving
      maximum earnings.
    """

    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Time must be a non-negative integer.")

    @lru_cache(maxsize=None)
    def solve(elapsed):

        if elapsed >= n:
            return 0, frozenset([(0, 0, 0)])

        best_profit = 0
        best_combinations = frozenset([(0, 0, 0)])

        for i, (_, duration, rate) in enumerate(BUILDINGS):

            finish_time = elapsed + duration

            if finish_time > n:
                continue

            # Earnings from the newly completed building
            profit = (n - finish_time) * rate

            # Calculate earnings from the remaining time
            future_profit, future_combinations = solve(finish_time)

            total_profit = profit + future_profit

            # Add the current building to every future combination
            current_combinations = frozenset(
                tuple(
                    count + (1 if j == i else 0)
                    for j, count in enumerate(combination)
                )
                for combination in future_combinations
            )

            # Update maximum earnings and valid combinations
            if total_profit > best_profit:

                best_profit = total_profit
                best_combinations = current_combinations

            elif total_profit == best_profit and total_profit > 0:

                best_combinations = (
                    best_combinations | current_combinations
                )

        return best_profit, best_combinations

    profit, combinations = solve(0)

    # Convert combinations into structured dictionaries
    combinations_list = [
        {
            "T": combination[0],
            "P": combination[1],
            "C": combination[2]
        }
        for combination in sorted(combinations)
    ]

    return {
        "time_units": n,
        "maximum_earnings": profit,
        "combinations": combinations_list
    }


def display_result(n):

    result = max_profit(n)

    print(f"\nInput time: {result['time_units']}")
    print(f"Maximum earnings: ${result['maximum_earnings']}")

    print("Valid Combinations:")

    for combination in result["combinations"]:

        print(
            f"  T: {combination['T']}, "
            f"P: {combination['P']}, "
            f"C: {combination['C']}"
        )

    print("-" * 40)


# Test assignment examples
for time_units in [7, 8, 13, 49]:
    display_result(time_units)


# Validate expected maximum earnings
assert max_profit(7)["maximum_earnings"] == 3000
assert max_profit(8)["maximum_earnings"] == 4500
assert max_profit(13)["maximum_earnings"] == 16500
assert max_profit(49)["maximum_earnings"] == 324000


# Validate all expected combinations for time unit 49
expected_49_combinations = [
    {"T": 8, "P": 2, "C": 0},
    {"T": 9, "P": 0, "C": 0}
]

assert (
    max_profit(49)["combinations"]
    == expected_49_combinations
), "Expected combinations do not match."


# Edge case validations
assert max_profit(0)["maximum_earnings"] == 0
assert max_profit(3)["maximum_earnings"] == 0
assert max_profit(4)["maximum_earnings"] == 0
assert max_profit(5)["maximum_earnings"] == 1000
assert max_profit(6)["maximum_earnings"] == 2000

# Validate input errors
try:
    max_profit(-1)
    raise AssertionError("Negative time should raise ValueError")
except ValueError:
    pass

try:
    max_profit(5.5)
    raise AssertionError("Float input should raise ValueError")
except ValueError:
    pass

print("\nAll Max Profit tests passed successfully!")
