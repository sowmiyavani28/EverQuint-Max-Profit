
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
    - Earnings start after construction is complete.
    - Each completed building continues earning until time n.
    - A building completed at time n earns zero.
    """

    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Time must be a non-negative integer.")

    @lru_cache(maxsize=None)
    def solve(elapsed):
        if elapsed >= n:
            return 0, (0, 0, 0)

        best_earnings = 0
        best_counts = (0, 0, 0)

        for i, (name, build_time, earning_rate) in enumerate(BUILDINGS):
            finish_time = elapsed + build_time

            # Cannot finish construction within the available time.
            if finish_time > n:
                continue

            # Earnings from this building after construction.
            current_earnings = (n - finish_time) * earning_rate

            # Earnings from buildings constructed afterward.
            future_earnings, future_counts = solve(finish_time)

            total_earnings = current_earnings + future_earnings

            counts = list(future_counts)
            counts[i] += 1
            counts = tuple(counts)

            if total_earnings > best_earnings:
                best_earnings = total_earnings
                best_counts = counts

        return best_earnings, best_counts

    earnings, counts = solve(0)

    return {
        "time_units": n,
        "earnings": earnings,
        "T": counts[0],
        "P": counts[1],
        "C": counts[2],
    }


def display_result(n):
    result = max_profit(n)

    print(f"Time Units       : {result['time_units']}")
    print(f"Maximum Earnings : ${result['earnings']}")
    print(f"Theatres (T)     : {result['T']}")
    print(f"Pubs (P)         : {result['P']}")
    print(f"Commercial (C)   : {result['C']}")
    print("-" * 35)


def run_tests():
    # Assignment test cases
    assert max_profit(7)["earnings"] == 3000
    assert max_profit(8)["earnings"] == 4500
    assert max_profit(13)["earnings"] == 16500

    # Edge cases
    assert max_profit(0)["earnings"] == 0
    assert max_profit(3)["earnings"] == 0
    assert max_profit(4)["earnings"] == 0

    # A theatre completed at time 5 earns nothing.
    # A pub completed at time 4 earns for one unit by time 5.
    assert max_profit(5)["earnings"] == 1000

    assert max_profit(6)["earnings"] == 2000

    # Invalid inputs
    for invalid_input in [-1, 2.5, "7", True]:
        try:
            max_profit(invalid_input)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Expected ValueError for {invalid_input!r}"
            )

    print("All tests passed successfully!\n")


if __name__ == "__main__":
    run_tests()

    print("EVERQUINT - MAX PROFIT PROBLEM")
    print("=" * 35)

    for time_units in [7, 8, 13]:
        display_result(time_units)
