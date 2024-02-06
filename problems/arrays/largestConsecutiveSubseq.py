

def largestConsecSubseq(arr):

    arr.sort()
    cnt = 1
    max1 = 0
    for i in range(1, len(arr)):
        if abs(arr[i - 1] - arr[i]) == 1:
            cnt += 1
            max1 = max(cnt, max1)
        else:
            cnt = 0

    return max1


arr = [1, 9, 3, 10, 4, 20, 2]

print(largestConsecSubseq(arr))
