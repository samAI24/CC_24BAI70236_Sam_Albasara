"""Brute-force solution for Frog Jump with K Distance.

This solution is intended for small inputs: it explores every valid path and
has exponential running time.
"""


class Solution:
    def minCost(self, height: list[int], k: int) -> int:
        if not height:
            raise ValueError("The height array must contain at least one stone.")
        if k < 1:
            raise ValueError("k must be at least 1.")

        def solve(i: int) -> int:
            if i == 0:
                return 0

            best = float("inf")
            for j in range(max(0, i - k), i):
                cost = solve(j) + abs(height[i] - height[j])
                best = min(best, cost)
            return int(best)

        return solve(len(height) - 1)


def read_integer(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError as error:
        raise ValueError("Please enter a valid integer.") from error


def main() -> None:
    print("Frog Jump with K Distance — Brute Force")
    print("Note: Brute force can take a very long time for larger inputs.")

    n = read_integer("Enter the number of stones: ")
    if not 1 <= n <= 100_000:
        raise ValueError("The number of stones must be between 1 and 100000.")

    try:
        height = [
            int(value)
            for value in input("Enter the stone heights, separated by spaces: ").split()
        ]
    except ValueError as error:
        raise ValueError("Please enter integer heights separated by spaces.") from error

    if len(height) != n:
        raise ValueError(f"Please enter exactly {n} heights.")
    if any(value < 0 or value > 10_000 for value in height):
        raise ValueError("Each height must be between 0 and 10000.")

    k = read_integer("Enter the maximum jump distance k: ")
    if k < 1:
        raise ValueError("k must be at least 1.")

    print(f"Minimum cost: {Solution().minCost(height, k)}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Input error: {error}")
