
def maxOccrBy2(arr):
    n = len(arr) // 2
    counter = {}
    for i in arr:
        if i in counter:
            counter[i] += 1
            if counter[i] > n:
                return i
        else:
            counter[i] = 1

print(maxOccrBy2([4,4,2,4,3,4,4,3,2,4]))