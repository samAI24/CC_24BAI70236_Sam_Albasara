def add_digits(num: int) -> int:
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num


def main() -> None:
    num = int(input("Enter a non-negative integer (0 to 2147483647): "))
    if not 0 <= num <= 2**31 - 1:
        print("Error: number must be between 0 and 2147483647.")
        return

    print("Digital root:", add_digits(num))


if __name__ == "__main__":
    main()
