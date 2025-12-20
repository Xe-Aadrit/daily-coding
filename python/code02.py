# Recursion practice

# Fibonacci Series using recursion
# n = number of the term
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# Sum of digits of a number
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

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
    print(" 1. Nth term of Fibonacci series\n 2. Sum of digits\n 3. Exit\n")
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

            # Validate numebr
            if validated_num == None:
                continue

            print(f"Sum of digits of {validated_num} is {sum_of_digits(validated_num)}.")

        case '3':
            # Exit the code
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Select one of the options given above.")