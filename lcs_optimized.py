def longest_common_subsequence(text1, text2):
    """Find the LCS length using a bottom-up dynamic-programming table."""
    rows = len(text1)
    columns = len(text2)
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[rows][columns]


def main():
    print("Longest Common Subsequence - Dynamic-Programming Method")
    print("Enter two strings to find the length of their LCS.")
    text1 = input("First string: ")
    text2 = input("Second string: ")

    result = longest_common_subsequence(text1, text2)
    print(f"\nLength of the longest common subsequence: {result}")
    print("Time complexity: O(m * n)")
    print("Space complexity: O(m * n)")


if __name__ == "__main__":
    main()
