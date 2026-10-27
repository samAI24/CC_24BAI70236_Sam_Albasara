"""Climbing Stairs using plain recursion, with GUI or terminal input."""

try:
    import tkinter as tk
except ImportError:
    tk = None


def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def calculate():
    try:
        n = int(entry.get())
        if not 1 <= n <= 45:
            raise ValueError
        if n > 25:
            result.set("Brute force is too slow for n > 25. Try the optimized program.")
            return
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

    root.title("Climbing Stairs - Brute Force")
    root.geometry("420x220")
    root.resizable(False, False)

    tk.Label(root, text="Climbing Stairs (Brute Force)",
             font=("Arial", 16, "bold")).pack(pady=15)
    tk.Label(root, text="Enter the number of steps (1-45):").pack()

    entry = tk.Entry(root, justify="center", font=("Arial", 12), width=12)
    entry.pack(pady=8)
    entry.insert(0, "5")
    entry.bind("<Return>", lambda _event: calculate())

    tk.Button(root, text="Calculate", command=calculate, width=15).pack(pady=5)

    result = tk.StringVar(value="Each move can be 1 or 2 steps.")
    tk.Label(root, textvariable=result, wraplength=380).pack(pady=8)

    root.mainloop()


def run_terminal():
    try:
        n = int(input("Enter the number of steps (1-45): "))
        if not 1 <= n <= 45:
            raise ValueError
        if n > 25:
            print("Brute force is too slow for n > 25. Try the optimized program.")
            return
        print(f"Number of ways: {climb_stairs(n)}")
    except ValueError:
        print("Enter a whole number from 1 to 45.")


if __name__ == "__main__":
    main()
