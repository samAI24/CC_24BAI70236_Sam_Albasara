class Queue:
    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1: self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else -1

    def peek(self):
        if not self.s2:
            while self.s1: self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else -1

    def display(self):
        arr = []
        if self.s2:
            arr = list(reversed(self.s2)) + self.s1
        else:
            arr = self.s1[:]
        if not arr:
            print("Queue: []")
        else:
            print("Queue:", arr)


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
        print(f"Size: {len(q.s1) + len(q.s2)}")
    elif ch == '5':
        q.display()
    elif ch == '6':
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please try again.")
