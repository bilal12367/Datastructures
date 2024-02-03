

def sumPairs(arr, k):
    s1 = {}
    ans = 0
    for i in range(len(arr)):
        b = k - arr[i]
        if b in s1:
            ans += s1[b]
        if arr[i] in s1:
            s1[arr[i]] += 1
        else:
            s1[arr[i]] = 1
    return ans


# print(sumPairs([1, 1, 1, 1], 2))
print(sumPairs([1, 5, 7, 1], 6))
