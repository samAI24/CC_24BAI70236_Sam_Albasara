def search_insert_optimized(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def main():
    nums = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))
    result = search_insert_optimized(nums, target)
    print("Insert position:", result)


if __name__ == "__main__":
    main()
