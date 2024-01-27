
fib = [0,1]
n = int(input('Enter the length of fibonacci series:'))

for i in range(n):
    sum = fib[i] + fib[i+1]
    fib.append(sum)

print(fib)