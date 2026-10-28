from random import choice
from typing import List


class Solution:
    """Optimized in-place DFS flood fill; changes visited land to water."""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1":
                    continue

                island_count += 1
                grid[row][col] = "0"
                stack = [(row, col)]

                while stack:
                    current_row, current_col = stack.pop()
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == "1"
                        ):
                            grid[next_row][next_col] = "0"
                            stack.append((next_row, next_col))

        return island_count


if __name__ == "__main__":
    grid = [[choice(("0", "1")) for _ in range(5)] for _ in range(5)]
    print("Approach: Optimized in-place DFS")
    print("Random input grid:")
    for row in grid:
        print(" ".join(row))
    print("Number of islands:", Solution().numIslands(grid))
