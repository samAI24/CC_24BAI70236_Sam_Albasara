def coin_change_optimized(coins: list[int], amount: int) -> int:
    """Return the minimum coin count using bottom-up dynamic programming."""
    unreachable = amount + 1
    dp = [unreachable] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1,
                )

    return dp[amount] if dp[amount] <= amount else -1


def main() -> None:
    print("Coin Change - Bottom-Up Dynamic Programming")

    try:
        coins = [int(value) for value in input(
            "Enter distinct positive coin denominations separated by spaces: "
        ).split()]
        amount = int(input("Enter the target amount (0-10000): "))

        if not 1 <= len(coins) <= 12:
            raise ValueError("enter between 1 and 12 coin denominations")
        if len(set(coins)) != len(coins):
            raise ValueError("coin denominations must be distinct")
        if any(coin < 1 or coin > 2**31 - 1 for coin in coins):
            raise ValueError("each coin must be between 1 and 2^31 - 1")
        if not 0 <= amount <= 10_000:
            raise ValueError("amount must be between 0 and 10000")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    result = coin_change_optimized(coins, amount)
    print(f"Minimum number of coins: {result}")


if __name__ == "__main__":
    main()
