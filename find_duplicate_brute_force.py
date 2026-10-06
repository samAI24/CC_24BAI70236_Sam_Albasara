def find_duplicate(nums):
    seen = set()

    for number in nums:
        if number in seen:
            return number
        seen.add(number)

    return -1


def read_numbers():
    values = input("Enter the numbers separated by spaces: ").split()
    try:
        nums = [int(value) for value in values]
    except ValueError:
        raise ValueError("Please enter integers only.") from None

    if len(nums) < 2:
        raise ValueError("Enter at least two numbers.")

    n = len(nums) - 1
    if any(number < 1 or number > n for number in nums):
        raise ValueError(f"Each number must be between 1 and {n}.")

    return nums


if __name__ == "__main__":
    try:
        numbers = read_numbers()
        print("Duplicate number:", find_duplicate(numbers))
    except ValueError as error:
        print("Invalid input:", error)