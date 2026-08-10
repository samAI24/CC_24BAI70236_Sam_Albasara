def search_insert_bruteforce(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def main():
    nums = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))
    result = search_insert_bruteforce(nums, target)
    print("Insert position:", result)


if __name__ == "__main__":
    main()
