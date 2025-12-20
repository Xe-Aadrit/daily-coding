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

# ------------ Main ------------

print("\ncode02/Aeon")
while True:
    print("\n------------ Menu ------------")
    print(" 1. Nth term of Fibonacci series\n 2. Sum of digits\n 3. Exit\n")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            # Fibonacci series function test
            n_th = int(input("Enter term number: "))
            print(f"{n_th}th term of the Fibonacci series is: {fibo(n_th)}.")

        case '2':
            # Sum of digits function test
            num = int(input("Enter number: "))
            print(f"Sum of digits of {num} is {sum_of_digits(num)}.")

        case '3':
            # Exit the code
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Select one of the options given above.")