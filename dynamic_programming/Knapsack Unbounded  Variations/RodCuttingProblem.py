
# Rod Cutting Problem

def unBoundedKnapsack(wtArr, valArr, W, n):
    t = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0

            if wtArr[i - 1] <= j:
                t[i][j] = max(valArr[i - 1] + t[i]  # We don't skip after we include the element
                              [j - wtArr[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][W]


if __name__ == '__main__':
    valArr = [1, 5, 8, 9, 10, 17, 17, 20]
    wtArr = [i for i in range(1, len(valArr)+1)]
    W = len(valArr)
    print(unBoundedKnapsack(wtArr, valArr, W, len(valArr)))
