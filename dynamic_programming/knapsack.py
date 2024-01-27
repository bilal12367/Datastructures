

def knapsack2dArr(wtArr, valArr, W, n):
    if W == 0 or n == 0:
        return 0
    
    if t[n][W] != -1:
        return t[n][W]

    if wtArr[n-1] <= W:
        t[n][W] = max(valArr[n-1] + knapsack2dArr(wtArr, valArr, W-wtArr[n-1], n-1), knapsack2dArr(wtArr, valArr, W, n-1))
        return t[n][W]
    else:
        t[n][W] = knapsack2dArr(wtArr, valArr, W, n-1)
        return t[n][W]
    
def knapsackMemoizeDict(wtArr, valArr, W, n):
    if W == 0 or n == 0:
        return 0
    x = n*W
    if x in td:
        return td[x]

    if wtArr[n-1] <= W:
        td[x] = max(valArr[n-1] + knapsackMemoizeDict(wtArr, valArr, W-wtArr[n-1], n-1), knapsackMemoizeDict(wtArr, valArr, W, n-1))
        return td[x]
    else:
        td[x] = knapsackMemoizeDict(wtArr, valArr, W, n-1)
        return td[x]

def knapsackTopDown(wtArr, valArr, W, n):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0  or j == 0:
                t[i][j] = 0
            elif wtArr[i-1] <= j:
                t[i][j] = max(valArr[i-1] + t[i-1][j-wtArr[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]


if __name__ == '__main__':
    # profit = [10, 32, 22, 43]
    profit = [10, 32, 22, 43]
    weight = [1, 2, 3, 4]
    W = 5
    n = len(profit)
    td = {}
    t = [[0 for i in range(W+1)] for j in range(n+1)]
    # t = [][]
    print(knapsackTopDown(weight, profit, W, n))
    print(t)
