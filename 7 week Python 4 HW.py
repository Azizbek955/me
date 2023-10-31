Numbers = []

while True:
    User_integer = input("Enter an integer (or 'done' to exit): ")

    if User_integer.lower() == 'done':
        break

    try:
        Number = int(User_integer)
        Numbers.append(Number)
        average = sum(Numbers) / len(Numbers)
        print(f"Average so far: {average}")
    except ValueError:
        print("Invalid input. Please enter an integer or 'done'.")

print("Program terminated.")
