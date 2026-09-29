class Solution(object):
    def searchRange(self, nums, target):

        # Function to find the FIRST position of target
        def findFirst():

            # Set binary search boundaries
            left, right = 0, len(nums) - 1

            # Store the answer
            ans = -1

            # Continue while search area is valid
            while left <= right:

                # Find middle index
                mid = (left + right) // 2

                # Target found
                if nums[mid] == target:
                    ans = mid

                    # Continue searching on the LEFT
                    # to find the first occurrence
                    right = mid - 1

                # Middle value is smaller than target
                elif nums[mid] < target:

                    # Search on the RIGHT side
                    left = mid + 1

                # Middle value is greater than target
                else:

                    # Search on the LEFT side
                    right = mid - 1

            # Return first occurrence
            return ans


        # Function to find the LAST position of target
        def findLast():

            # Set binary search boundaries
            left, right = 0, len(nums) - 1

            # Store the answer
            ans = -1

            # Continue while search area is valid
            while left <= right:

                # Find middle index
                mid = (left + right) // 2

                # Target found
                if nums[mid] == target:
                    ans = mid

                    # Continue searching on the RIGHT
                    # to find the last occurrence
                    left = mid + 1

                # Middle value is smaller than target
                elif nums[mid] < target:

                    # Search on the RIGHT side
                    left = mid + 1

                # Middle value is greater than target
                else:

                    # Search on the LEFT side
                    right = mid - 1

            # Return last occurrence
            return ans


        # Return first and last positions
        return [findFirst(), findLast()]




nums = [5, 7, 7, 8, 8, 10]
target = 8

# Create Solution object
solution = Solution()

# Call searchRange()
result = solution.searchRange(nums, target)

# Print the result
print(result)