def fibonacci(n):
    a , b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
n = int(input("Enter n: "))
print("The", n, "th Fibonacci number is:", fibonacci(n))