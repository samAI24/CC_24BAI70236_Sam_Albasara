def add_digits(num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


def main() -> None:
    num = int(input("Enter a non-negative integer (0 to 2147483647): "))
    if not 0 <= num <= 2**31 - 1:
        print("Error: number must be between 0 and 2147483647.")
        return

    print("Digital root:", add_digits(num))


if __name__ == "__main__":
    main()
