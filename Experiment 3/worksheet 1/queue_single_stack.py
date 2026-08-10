class Queue:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if not self.s:
            return -1
        t = self.s.pop()
        if not self.s:
            return t
        res = self.pop()
        self.s.append(t)
        return res

    def peek(self):
        if not self.s:
            return -1
        t = self.s.pop()
        res = t if not self.s else self.peek()
        self.s.append(t)
        return res

    def display(self):
        if not self.s:
            print("Queue: []")
        else:
            print("Queue:", self.s)


q = Queue()
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
        q.push(value)
        print(f"Enqueued: {value}")
    elif ch == '2':
        result = q.pop()
        print(f"Dequeued: {result}")
    elif ch == '3':
        print(f"Front: {q.peek()}")
    elif ch == '4':
        print(f"Size: {len(q.s)}")
    elif ch == '5':
        q.display()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
