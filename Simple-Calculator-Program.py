
# Python program for Simple calculator

def calculator():
    print(" It is a Simple Calculator")
    print("Choose 1 for Addition")
    print("Choose 2 for Subtraction")
    print("Choose 3 for Multiplication")
    print("Choose 4 for Division")
    print("Choose 5 for Modulo")

    choice = input("Enter your choice (1/2/3/4/5): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if (choice == '1'):
        print("The addition of", num1, "+", num2, "=", num1 + num2)

    elif (choice == '2'):
        print("The substraction of", num1, "-", num2, "=", num1 - num2)

    elif (choice == '3'):
        print("The multiplication of ", num1, "*", num2, "=", num1 * num2)

    elif (choice == '4'):
        if (num2 != 0):
            print("The division of", num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    elif (choice == '5'):
        if (num2 != 0):
            print("The modulo of", num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Modulo by zero is not allowed.")

    else:
        print("The choice Invalid.")

calculator()
