class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_list(slow)

    p1 = head
    p2 = second_half
    result = True
    while p2:
        if p1.val != p2.val:
            result = False
            break
        p1 = p1.next
        p2 = p2.next

    reverse_list(second_half)
    return result


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
    if raw_input is None:
        return []

    text = raw_input.strip()
    if not text:
        return []

    normalized = text.replace(",", " ")
    try:
        return list(map(int, normalized.split()))
    except ValueError:
        raise ValueError("Please enter only integer values separated by spaces or commas.")


def print_list(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements) if elements else "[]")


def main():
    print("=== Part 2: Palindrome Linked List (Optimized O(1) Space) ===")
    user_input = input("Enter values: ")

    try:
        values = parse_values(user_input)
    except ValueError as e:
        print(f"Error: {e}")
        return

    if not values:
        print("No values entered. Please enter at least one number.")
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
