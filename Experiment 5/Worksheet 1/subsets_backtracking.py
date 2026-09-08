class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(start, current_subset):
            result.append(current_subset[:])

            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements separated by spaces: ").split()))
    print(Solution().subsets(nums))
