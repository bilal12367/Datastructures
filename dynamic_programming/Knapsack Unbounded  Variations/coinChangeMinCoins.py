import sys

# Utility function for solving the minimum coins problem


def minCoinsUtil(coins, m, V, dp):
    # Base case: If target value V is 0, no coins are needed
    if V == 0:
        return 0

    # If subproblem is already solved, return the result from DP table
    if dp[V] != -1:
        return dp[V]

    res = sys.maxsize

    # Iterate over all coins and recursively solve for subproblems
    for i in range(m):
        if coins[i] <= V:
            # Recursive call to solve for remaining value V - coins[i]
            sub_res = minCoinsUtil(coins, m, V - coins[i], dp)

            # If the subproblem has a valid solution and the total number of coins
            # is smaller than the current result, update the result
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    # Save the result in the DP table
    dp[V] = res

    return res


def minCoinsAditya(coins, n, target):
    t = [[0 for i in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = sys.maxsize - 1

            if i == 1:
                if j % coins[i - 1] == 0:
                    t[i][j] = j / coins[i - 1]
                else:
                    t[i][j] = sys.maxsize - 1
    t[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, target+1):
            if coins[i - 1] <= j:
                t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][target]
# Function to find the minimum number of coins needed to make a target value


def minCoins(coins, m, V):
    # Create a DP table to store results of subproblems
    dp = [-1] * (V + 1)

    # Call the utility function to solve the problem
    return minCoinsUtil(coins, m, V, dp)


# Driver code
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    res = minCoinsAditya(coins, m - 1, V)

    if res == sys.maxsize:
        res = -1

    # Find the minimum number of coins required
    print("Minimum coins required is", res)
