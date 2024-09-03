#function that returns the factorial of a non-negative integer.

def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

result = calculate_factorial(3)
print(result)