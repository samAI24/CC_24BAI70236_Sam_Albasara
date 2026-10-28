def is_subsequence(candidate, text):
    """Return whether candidate appears in text in the same character order."""
    candidate_index = 0

    for character in text:
        if candidate_index < len(candidate) and character == candidate[candidate_index]:
            candidate_index += 1

    return candidate_index == len(candidate)


def longest_common_subsequence(text1, text2):
    """Find the LCS length by checking every subsequence of the shorter string."""
    shorter, longer = sorted((text1, text2), key=len)
    longest_length = 0

    for mask in range(1 << len(shorter)):
        candidate = "".join(
            shorter[index]
            for index in range(len(shorter))
            if mask & (1 << index)
        )

        if len(candidate) > longest_length and is_subsequence(candidate, longer):
            longest_length = len(candidate)

    return longest_length


def main():
    print("Longest Common Subsequence - Brute-Force Method")
    print("Enter two strings to find the length of their LCS.")
    text1 = input("First string: ")
    text2 = input("Second string: ")

    result = longest_common_subsequence(text1, text2)
    print(f"\nLength of the longest common subsequence: {result}")
    print("Time complexity: O(2^s * l), where s is the shorter length and l is the longer length.")
    print("Space complexity: O(s), for the candidate subsequence.")


if __name__ == "__main__":
    main()
