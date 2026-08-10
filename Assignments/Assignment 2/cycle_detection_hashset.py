class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list_with_cycle(values, cycle_pos):
    if not values:
        return None, None

    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    cycle_node = None
    if 0 <= cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
        cycle_node = nodes[cycle_pos]

    return nodes[0], cycle_node

def detect_cycle_hashset(head):
    visited = set()
    curr = head
    step = 1
    logs = []

    while curr:
        node_id = id(curr)
        logs.append(f"Step {step}: Visiting Node(value={curr.value}, id={hex(node_id)})")
        
        if curr in visited:
            logs.append(f"-> Cycle Detected! Node(value={curr.value}) was already visited.")
            return True, logs
        
        visited.add(curr)
        curr = curr.next
        step += 1

    logs.append("-> Reached end of Linked List (None). No cycle detected.")
    return False, logs

def print_list_preview(values, cycle_pos):
    if not values:
        print("List: Empty")
        return
    
    representation = " -> ".join(map(str, values))
    if 0 <= cycle_pos < len(values):
        print(f"List Structure: {representation}")
        print(f"Cycle connected from tail ({values[-1]}) -> Index {cycle_pos} (Value: {values[cycle_pos]})")
    else:
        print(f"List Structure: {representation} -> None")
        print("Cycle: None (Linear List)")

def main():
    print("=" * 60)
    print("      LINKED LIST CYCLE DETECTION USING HASHSET")
    print("=" * 60)

    while True:
        try:
            raw_input = input("\nEnter space-separated numbers for linked list nodes (e.g. 1 2 3 4 5): ").strip()
            if not raw_input:
                print("Invalid input! Please enter at least one number.")
                continue
            
            values = list(map(int, raw_input.split()))
            
            print(f"\nNodes count: {len(values)}")
            cycle_pos = int(input(f"Enter 0-based index to connect tail for cycle (-1 for no cycle, 0 to {len(values)-1}): ").strip())

            if cycle_pos >= len(values) or cycle_pos < -1:
                print(f"Invalid cycle position! Must be between -1 and {len(values)-1}.")
                continue

            head, _ = create_linked_list_with_cycle(values, cycle_pos)
            
            print("\n--- LINKED LIST CONFIGURATION ---")
            print_list_preview(values, cycle_pos)

            print("\n--- EXECUTION TRACE (HashSet Method) ---")
            has_cycle, logs = detect_cycle_hashset(head)
            for log in logs:
                print(log)

            print("\n--- RESULT ---")
            if has_cycle:
                print("Result: CYCLE DETECTED in the linked list!")
            else:
                print("Result: NO CYCLE detected in the linked list.")

        except ValueError:
            print("Invalid input format! Please enter valid integers.")

        choice = input("\nWould you like to test another case? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting HashSet Cycle Detection Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
