class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    if head is None:
        return None

    odd = []
    even = []
    current = head
    position = 1

    while current:
        if position % 2 == 1:
            odd.append(current.val)
        else:
            even.append(current.val)

        current = current.next
        position += 1

    values = odd + even
    current = head
    i = 0
    while current:
        current.val = values[i]
        current = current.next
        i += 1
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
    print("=== Odd-Even Linked List (Simple) ===")
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
