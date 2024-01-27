import sys



arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 100, 101, 101, 102]

## Better Approach
# longest = 0
# if len(arr) != 0:
#     longest = 1
# lastSmaller = arr[0]
# cnt = 1
# for i in range(1,len(arr)):
#     if arr[i] == lastSmaller + 1:
#         cnt += 1
#         lastSmaller = arr[i]
#     elif arr[i] != lastSmaller:
#         cnt = 1
#         lastSmaller = arr[i]
    
#     longest = max(longest, cnt)

# print(longest)


## Optimal Approach
st = set(arr)
longest = sys.maxsize * -1 - 1
for i in st:
    if (i - 1) not in st:
        cnt = 1
        while i + 1 in st:
            cnt += 1
            i += 1
        if cnt > longest:
            longest = cnt
print(longest)
