from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = set()

        def backtrack(remaining: int, current: List[int]) -> None:
            if remaining == 0:
                combinations.add(tuple(sorted(current)))
                return
            if remaining < 0:
                return

            for candidate in candidates:
                current.append(candidate)
                backtrack(remaining - candidate, current)
                current.pop()

        backtrack(target, [])
        return [list(combination) for combination in sorted(combinations)]


if __name__ == "__main__":
    candidates = list(map(int, input("Enter candidates separated by spaces: ").split()))
    target = int(input("Enter target: "))
    print("Result:", Solution().combinationSum(candidates, target))