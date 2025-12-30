# Recursion practice

# 1. Fibonacci Series using recursion
# n = number of the term
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# 2. Sum of digits of a number
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# 3. Factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

# 4. HCF of 2 numbers
def hcf(a, b):
    r = a % b
    if r == 0:
        return b
    return hcf(b, a%b)

# User-input validator
def validate_number(user_input):
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. PLease enter an integer.")
        return

# ------------ Main ------------

print("\ncode02/Aeon")
while True:
    print("\n------------ Menu ------------")
    print(" 1. Nth term of Fibonacci series\n 2. Sum of digits\n 3. Factorial\n 4. HCF\n 5. Exit\n")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            # Fibonacci series function test
            n_th = input("Enter term number: ")
            validated_term = validate_number(n_th)

            # Validate term
            if validated_term == None:
                continue

            print(f"{validated_term}th term of the Fibonacci series is: {fibo(validated_term)}.")

        case '2':
            # Sum of digits function test
            num = input("Enter number: ")
            validated_num = validate_number(num)

            # Validate number
            if validated_num == None:
                continue

            print(f"Sum of digits of {validated_num} is {sum_of_digits(validated_num)}.")

        case '3':
            # Factorial function test
            num = input("Enter number: ")
            validated_num = validate_number(num)

            # Validate number
            if validated_num == None:
                continue

            print(f"Sum of digits of {validated_num} is {fact(validated_num)}.")

        case '4':
            # HCF of two numbers
            # Number 1
            x = input("Enter number 1: ")
            validated_num1 = validate_number(x)

            # Validate first number
            if validated_num1 == None:
                continue

            # Number 2
            y = input("Enter number 2: ")
            validated_num2 = validate_number(y)

            # Validate second number
            if validated_num2 == None:
                continue

            hcf_of_numbers = hcf(validated_num1, validated_num2)
            print(f"HCF of {validated_num1} and {validated_num2} is {hcf_of_numbers}")

        case '5':
            # Exit the code
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Select one of the options given above.")