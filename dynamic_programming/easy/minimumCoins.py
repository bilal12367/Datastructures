

def min_coins(temp, coins,n,target):
    if target == 0:
        print(temp," ret 0")
        return 0
    if target < 0 or n == 0:
        print(temp," ret inf")
        return float('inf')
    temp.append(coins[n - 1])
    return min(1 + min_coins(temp, coins, n - 1, target - coins[n - 1]), min_coins(temp,coins, n -1 ,target - coins[n - 1]))
arr = [1,2,5]
target = 11
print(min_coins([], arr, len(arr),target))