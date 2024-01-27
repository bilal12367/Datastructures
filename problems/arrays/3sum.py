
arr = [-1, 0, 1, 2, -1, -4]
target = 0
st = []
arr.sort()
for i in range(len(arr)):
    j = i + 1
    k = len(arr) - 1
    if j != i + 1 and arr[j] == arr[j-1]:
        continue
    while (j < k):
        sum = arr[i]
        sum += arr[j]
        sum += arr[k]
        if sum == target:
            st.append([arr[i], arr[j], arr[k]])
            j += 1
            k -= 1
            while j < k and arr[j] == arr[j-1]:
                j += 1

            while k > j and k+1 <= len(arr)-1 and arr[k] == arr[k+1]:
                k += 1

        elif sum < target:
            j += 1
        elif sum > target:
            k -= 1
print(st)
