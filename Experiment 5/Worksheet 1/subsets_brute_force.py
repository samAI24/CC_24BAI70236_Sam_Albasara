class Solution(object):
    def subsets(self, nums):
        result = []
        n = len(nums)

        # Generate every possible bitmask.
        for mask in range(1 << n):
            current_subset = []

            for i in range(n):
                if mask & (1 << i):
                    current_subset.append(nums[i])

            result.append(current_subset)

        return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements separated by spaces: ").split()))
    print(Solution().subsets(nums))
