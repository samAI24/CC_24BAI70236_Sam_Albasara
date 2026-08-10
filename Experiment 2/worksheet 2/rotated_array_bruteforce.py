def search_bruteforce(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def main():
    nums = list(map(int, input("Enter rotated numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))
    result = search_bruteforce(nums, target)
    print("Index:", result)


if __name__ == "__main__":
    main()
