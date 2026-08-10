class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list_with_cycle(values, cycle_pos):
    if not values:
        return None

    nodes = [Node(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if 0 <= cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


def detect_cycle_floyd(head):
    if not head or not head.next:
        return False, ["List has fewer than 2 nodes -> no cycle."]

    slow = head
    fast = head
    logs = []
    step = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        step += 1
        logs.append(f"Step {step}: slow={slow.value}, fast={fast.value}")

        if slow == fast:
            logs.append(f"Cycle detected: slow and fast meet at Node({slow.value}).")
            return True, logs

    logs.append("Fast pointer reached the end -> no cycle.")
    return False, logs


def print_list_preview(values, cycle_pos):
    if not values:
        print("List: Empty")
        return

    print("List Structure:", " -> ".join(map(str, values)))
    if 0 <= cycle_pos < len(values):
        print(f"Tail connects back to index {cycle_pos} (value {values[cycle_pos]})")
    else:
        print("Cycle: None")


def main():
    print("=" * 60)
    print("   FLOYD'S CYCLE DETECTION")
    print("=" * 60)

    while True:
        try:
            values = input("\nEnter numbers separated by spaces: ").strip()
            if not values:
                print("Please enter at least one number.")
                continue

            numbers = list(map(int, values.split()))
            cycle_pos = int(input(f"Enter cycle start index (-1 for no cycle, 0 to {len(numbers) - 1}): ").strip())

            if cycle_pos < -1 or cycle_pos >= len(numbers):
                print(f"Invalid cycle position! Use a value from -1 to {len(numbers) - 1}.")
                continue

            head = create_linked_list_with_cycle(numbers, cycle_pos)
            print_list_preview(numbers, cycle_pos)

            has_cycle, logs = detect_cycle_floyd(head)
            for log in logs:
                print(log)

            if has_cycle:
                print("Result: CYCLE DETECTED")
            else:
                print("Result: NO CYCLE")

        except ValueError:
            print("Invalid input. Please enter integers only.")

        choice = input("\nTry another case? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
