from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []

        def backtrack(start: int, remaining: int, current: List[int]) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            for index in range(start, len(candidates)):
                candidate = candidates[index]
                if candidate > remaining:
                    break

                current.append(candidate)
                backtrack(index, remaining - candidate, current)
                current.pop()

        backtrack(0, target, [])
        return result


if __name__ == "__main__":
    candidates = list(map(int, input("Enter candidates separated by spaces: ").split()))
    target = int(input("Enter target: "))
    print("Result:", Solution().combinationSum(candidates, target))