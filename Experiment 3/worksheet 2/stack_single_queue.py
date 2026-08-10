q = []


def push(x):
    q.append(x)
    for _ in range(len(q) - 1):
        q.append(q.pop(0))


def display_stack():
    if not q:
        print("Stack: []")
    else:
        print("Stack:", q)


while True:
    print("\n===== Stack Operations =====")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Size")
    print("5. Display")
    print("6. Exit")
    ch = input("Choose an option: ")

    if ch == '1':
        value = int(input("Enter value: "))
        push(value)
        print(f"Pushed: {value}")
    elif ch == '2':
        if q:
            removed = q.pop(0)
            print(f"Popped: {removed}")
        else:
            print("Popped: -1")
    elif ch == '3':
        if q:
            print(f"Top: {q[0]}")
        else:
            print("Top: -1")
    elif ch == '4':
        print(f"Size: {len(q)}")
    elif ch == '5':
        display_stack()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
