
def knapsack(wt, Val, C, n):
    t = [[-1 for _ in range(C + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i - 1] <= j:
                t[i][j] = max(Val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    print(t)
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
    print(knapsack(weight, profit, W, n))
