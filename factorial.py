def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    num = 5   # change this number to test
    print(f"Factorial of {num} is {factorial(num)}")
