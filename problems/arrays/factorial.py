
def factorial(num):
    fact=1
    for i in range(num):
        fact = fact * num
        num = num -1
    return fact

print(factorial(int(input('Enter number to find factorial: '))))