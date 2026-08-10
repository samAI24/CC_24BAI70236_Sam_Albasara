st = []


def display_stack():
    if not st:
        print("Stack: []")
    else:
        print("Stack:", st)


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
        st.append(value)
        print(f"Pushed: {value}")
    elif ch == '2':
        if st:
            removed = st.pop()
            print(f"Popped: {removed}")
        else:
            print("Popped: -1")
    elif ch == '3':
        if st:
            print(f"Top: {st[-1]}")
        else:
            print("Top: -1")
    elif ch == '4':
        print(f"Size: {len(st)}")
    elif ch == '5':
        display_stack()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
