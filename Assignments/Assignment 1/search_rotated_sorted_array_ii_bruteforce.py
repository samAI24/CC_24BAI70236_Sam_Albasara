def search_bruteforce(nums, target):
    for index, value in enumerate(nums):
        if value == target:
            return True, index
    return False, -1


def main():
    nums_input = input("Enter the array numbers separated by spaces: ")
    target = int(input("Enter the target value: "))

    nums = list(map(int, nums_input.split()))
    found, position = search_bruteforce(nums, target)

    print(f"Array: {nums}")
    print(f"Target: {target}")
    print(f"Found: {found}")
    print(f"Position: {position}")


if __name__ == "__main__":
    main()
