from random import choice
from typing import List


class Solution:
    """Basic DFS approach using a separate visited matrix."""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1" or visited[row][col]:
                    continue

                island_count += 1
                stack = [(row, col)]
                visited[row][col] = True

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
                            and not visited[next_row][next_col]
                        ):
                            visited[next_row][next_col] = True
                            stack.append((next_row, next_col))

        return island_count


if __name__ == "__main__":
    grid = [[choice(("0", "1")) for _ in range(5)] for _ in range(4)]
    print("Approach: Basic DFS with a visited matrix")
    print("Random input grid:")
    for row in grid:
        print(" ".join(row))
    print("Number of islands:", Solution().numIslands(grid))
