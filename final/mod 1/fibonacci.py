n = int(input("Enter the value of n: "))

if n == 0:
    fib_series = [0]
elif n == 1:
    fib_series = [0, 1]
else:
    fib_series = [0, 1]  # Initialize Fibonacci series with the first two numbers
    while fib_series[-1] + fib_series[-2] <= n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)

print("Fibonacci series up to", n, ":", fib_series)
