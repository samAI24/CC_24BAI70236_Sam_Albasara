def search_optimized(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True, mid

        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        else:
            left += 1

    return False, -1


def main():
    nums_input = input("Enter the array numbers separated by spaces: ")
    target = int(input("Enter the target value: "))

    nums = list(map(int, nums_input.split()))
    found, position = search_optimized(nums, target)

    print(f"Array: {nums}")
    print(f"Target: {target}")
    print(f"Found: {found}")
    print(f"Position: {position}")


if __name__ == "__main__":
    main()
