q1, q2 = [], []


def push(x):
    global q1, q2
    q2.append(x)
    while q1: q2.append(q1.pop(0))
    q1, q2 = q2, q1


def display_stack():
    if not q1:
        print("Stack: []")
    else:
        print("Stack:", q1)


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
        if q1:
            removed = q1.pop(0)
            print(f"Popped: {removed}")
        else:
            print("Popped: -1")
    elif ch == '3':
        if q1:
            print(f"Top: {q1[0]}")
        else:
            print("Top: -1")
    elif ch == '4':
        print(f"Size: {len(q1)}")
    elif ch == '5':
        display_stack()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
