"""Climbing Stairs using bottom-up DP, with GUI or terminal input."""

try:
    import tkinter as tk
except ImportError:
    tk = None


def climb_stairs(n):
    if n <= 2:
        return n

    previous_one, previous_two = 1, 2
    for _ in range(3, n + 1):
        previous_one, previous_two = previous_two, previous_one + previous_two
    return previous_two


def calculate():
    try:
        n = int(entry.get())
        if not 1 <= n <= 45:
            raise ValueError
        result.set(f"Number of ways: {climb_stairs(n)}")
    except ValueError:
        result.set("Enter a whole number from 1 to 45.")


def main():
    global entry, result

    if tk is None:
        run_terminal()
        return

    try:
        root = tk.Tk()
    except tk.TclError:
        run_terminal()
        return

    root.title("Climbing Stairs - Optimized")
    root.geometry("420x220")
    root.resizable(False, False)

    tk.Label(root, text="Climbing Stairs (Optimized DP)",
             font=("Arial", 16, "bold")).pack(pady=15)
    tk.Label(root, text="Enter the number of steps (1-45):").pack()

    entry = tk.Entry(root, justify="center", font=("Arial", 12), width=12)
    entry.pack(pady=8)
    entry.insert(0, "5")
    entry.bind("<Return>", lambda _event: calculate())

    tk.Button(root, text="Calculate", command=calculate, width=15).pack(pady=5)

    result = tk.StringVar(value="Time: O(n)  |  Extra space: O(1)")
    tk.Label(root, textvariable=result, wraplength=380).pack(pady=8)

    root.mainloop()


def run_terminal():
    try:
        n = int(input("Enter the number of steps (1-45): "))
        if not 1 <= n <= 45:
            raise ValueError
        print(f"Number of ways: {climb_stairs(n)}")
    except ValueError:
        print("Enter a whole number from 1 to 45.")


if __name__ == "__main__":
    main()
