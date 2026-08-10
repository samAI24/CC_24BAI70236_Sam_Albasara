class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def main():
    print("=== Odd-Even Linked List (Optimized) ===")
    user_input = input("Enter numbers separated by spaces: ").strip()

    if not user_input:
        print("No numbers entered.")
        return

    try:
        values = [int(x) for x in user_input.split()]
    except ValueError:
        print("Please enter only integer values.")
        return

    head = build_list(values)
    print(f"Original list: {to_list(head)}")

    result = odd_even_list(head)
    print(f"Reordered list: {to_list(result)}")


if __name__ == "__main__":
    main()
