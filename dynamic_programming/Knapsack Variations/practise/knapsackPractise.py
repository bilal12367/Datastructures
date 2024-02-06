
def knapsack(wtArr, valArr, W, n):
    if W == 0 or n == 0:
        return 0
    elif wtArr[n-1] <= W:
        return max(valArr[n-1] + knapsack(wtArr,valArr,W-wtArr[n-1],n-1), knapsack(wtArr, valArr, W, n-1))
    else:
        return knapsack(wtArr,valArr,W,n-1)

def knapsackTopDown(wtArr,valArr, W, n):
    t = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if j == 0 or i == 0:
                t[i][j] = 0
            elif wtArr[i-1] <= j:
                t[i][j] = max(valArr[i-1] + t[j - wtArr[i-1]][i-1] , t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]

if __name__ == '__main__':
    profit = [10, 32, 22, 43]
    weight = [1, 2, 3, 4]
    W = 5
    print(knapsack(weight, profit, W, len(weight)))
