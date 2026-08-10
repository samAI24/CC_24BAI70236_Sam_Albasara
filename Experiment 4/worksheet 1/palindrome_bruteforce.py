
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    if not head:
        return True

    vals = []
    curr = head

    while curr:
        vals.append(curr.val)
        curr = curr.next

    return vals == vals[::-1]


def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def parse_values(raw_input):
    text = raw_input.strip()

    if not text:
        return []

    # If spaces or commas are present, treat them as separators
    if " " in text or "," in text:
        normalized = text.replace(",", " ")
        return list(map(int, normalized.split()))

    # Otherwise, treat each digit as a separate node
    return [int(digit) for digit in text]


def print_list(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(elements))


def main():
    print("=== Part 1: Palindrome Linked List (Brute Force) ===")

    user_input = input("Enter values: ")

    try:
        values = parse_values(user_input)
    except ValueError:
        print("Error: Please enter only integer values.")
        return

    if not values:
        print("No values entered.")
        return

    head = create_linked_list(values)

    print("\nLinked List:")
    print_list(head)

    if is_palindrome(head):
        print("Result: Palindrome")
    else:
        print("Result: NOT a Palindrome")


if __name__ == "__main__":
    main()