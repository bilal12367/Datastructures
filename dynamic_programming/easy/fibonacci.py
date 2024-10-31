
memo = {}

def fibonacci(n):
    print(n, end=" , ")
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    
    print(n, end=" , ")
    if n <= 2:
        memo[n] = 1
        return memo[n]
    
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]

print(fibonacci_memo(7))