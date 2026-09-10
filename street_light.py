```python
# Automatic Street Light Simulation

print("=== Automatic Street Light System ===")

while True:
    print("\nSelect the light condition:")
    print("1. Dark")
    print("2. Bright")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("It is DARK.")
        print("Street Light: ON")

    elif choice == "2":
        print("It is BRIGHT.")
        print("Street Light: OFF")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
```
