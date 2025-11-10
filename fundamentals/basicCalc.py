import time

def addition(a, b):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a + b
        print(f"Addition result: {result}")
        time.sleep(2)
    except ValueError:
        print("Invalid input. Please enter a number.")

def subtraction(a, b):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a - b
        print(f"Subtraction result: {result}")
        time.sleep(2)
    except ValueError:
        print("Invalid input. Please enter a number.")

def multiplication(a, b):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a * b
        print(f"Multiplication result: {result}")
        time.sleep(2)
    except ValueError:
        print("Invalid input. Please enter a number.")

def division(a, b):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a / b
        print(f"Division result: {result}")
        time.sleep(2)
    except ZeroDivisionError:
        print("ERROR: Do not divide by zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")

options = [
    "1. Addition",
    "2. Subtraction",
    "3. Multiplication",
    "4. Division",
    "5. Exit"
]

while True:
    print("\n", "="*5, "BASIC CLI PYTHON CALCULATOR", "="*5)
    for i in options:
        print(i)
    
    try:
        choice = int(input("\nChoose an option: "))
        
        if 1 <= choice <= 5:
            if choice == 1:
                addition(0, 0)
            elif choice == 2:
                subtraction(0, 0)
            elif choice == 3:
                multiplication(0, 0)
            elif choice == 4:
                division(0, 0)
            elif choice == 5:
                break
        else:
            print(f"ERROR: Option {choice} not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
