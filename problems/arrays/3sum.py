
arr = [-1, 0, 1, 2, -1, -4]
target = 0
st = []
arr.sort()
print(arr)
def three_sum(arr, target):
    n = len(arr)
    res = []
    for i in range(n):
        if i != 0 and arr[i - 1] == arr[i]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
            else:
                res.append(([i,j,k],[arr[i],arr[j],arr[k]]))
                j += 1
                k -= 1
            while j<k and arr[j] == arr[j - 1]:
                j += 1
            while k + 1 < n and arr[k] == arr[k + 1]:
                k -= 1
    return res
        
print(three_sum(arr, 0))
