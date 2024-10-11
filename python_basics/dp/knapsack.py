
wtArr = [2,3,4,5]
values = [3,4,8,8]
cap = 6
t = [[-1 for i in range(cap+1)] for _ in range(len(values)+1)]
def knapsack(wtArr, values, W, n):
    print(wtArr[:n])
    if n == 0 or W == 0:
        t[n][W] = 0
        return t[n][W]
    if t[n][W] != -1:
        return t[n][W]
    elif wtArr[n-1] < W:
        t[n][W] = max( values[n-1] + knapsack(wtArr, values, W - wtArr[n-1], n - 1), knapsack(wtArr, values, W, n-1) )
        return t[n][W]
    else:
        t[n][W] = knapsack(wtArr, values, W, n-1)
        return t[n][W]
    
    
s= "bbaabgbgb"
j = "bag"
def lettersKs(s, n, comb):
    if n < 0:
        return 0
    cnt = 0
    if("".join(comb) == j):
        cnt = 1
    include = lettersKs(s,n-1,[ s[n-1]]+comb)
    exclude = lettersKs(s, n-1, comb)
    return cnt + int(include) + int(exclude)
        
print(lettersKs(s,len(s),[]))
# knapsack(wtArr,values, cap, len(values))
# print(t)
# print("Res = ",t[len(values)][cap])



