q = []


def display_queue():
    if not q:
        print("Queue: []")
    else:
        print("Queue:", q)


while True:
    print("\n===== Queue Operations =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Size")
    print("5. Display")
    print("6. Exit")
    ch = input("Choose an option: ")

    if ch == '1':
        value = int(input("Enter value: "))
        q.append(value)
        print(f"Enqueued: {value}")
    elif ch == '2':
        if q:
            removed = q.pop(0)
            print(f"Dequeued: {removed}")
        else:
            print("Dequeued: -1")
    elif ch == '3':
        if q:
            print(f"Front: {q[0]}")
        else:
            print("Front: -1")
    elif ch == '4':
        print(f"Size: {len(q)}")
    elif ch == '5':
        display_queue()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
