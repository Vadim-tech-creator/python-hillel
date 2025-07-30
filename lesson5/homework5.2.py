while True:
    num_1 = float(input("Enter first number:"))
    char = input("Operation: ")
    num_2 = float(input("Enter second number: "))

    if char == "+":
        result = num_1 + num_2
        print(result)
    elif char == "-":
        result = num_1 - num_2
        print(result)
    elif char == "*":
        result = num_1 * num_2
        print(result)
    elif char == "/":
        if num_2 != 0:
            result = num_1 / num_2
            print(result)
        else:
            print("Error")
    else:
        print("Unknown operation")

    again = input("Do you want to continue?")
    if again.lower() != "y":
        break