

def knapsack(WtArr, valArr, W, n):

    if W == 0 or n == 0:
        return 0

    if WtArr[n-1] <= W:
        return max(valArr[n-1] + knapsack(WtArr, valArr, W - WtArr[n-1], n - 1), knapsack(WtArr, valArr, W, n-1))
    else:
        return knapsack(WtArr, valArr, W, n-1)


def knapsackDP(WtArr, valArr, W, n):
    t = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if j == 0 or i == 0:
                t[i][j] = 0

            if WtArr[i-1] <= j:
                t[i][j] = max(valArr[i-1] + t[i-1][j - WtArr[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]


# Test Case 1
weights1 = [2, 5, 1, 4, 3]
values1 = [10, 5, 15, 7, 6]
capacity1 = 8
expected_output1 = 22
print(knapsackDP(weights1, values1, capacity1, len(weights1) - 1))

# Test Case 2
weights2 = [3, 2, 4, 1]
values2 = [6, 8, 7, 2]
capacity2 = 5
expected_output2 = 13

# Test Case 3
weights3 = [1, 3, 4, 5]
values3 = [1, 4, 5, 7]
capacity3 = 7
expected_output3 = 9

# Test Case 4
weights4 = [2, 2, 2, 5, 5, 8, 7, 10]
values4 = [5, 5, 2, 10, 7, 6, 12, 15]
capacity4 = 10
expected_output4 = 29

# Test Case 5
weights5 = [1, 2, 3, 4, 5]
values5 = [2, 5, 9, 5, 3]
capacity5 = 7
expected_output5 = 14

# Test Case 6
weights6 = [10, 20, 30]
values6 = [60, 100, 120]
capacity6 = 50
expected_output6 = 220
