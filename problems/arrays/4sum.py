
arr = [1, 0, -1, 0, -2, 2]
target = 0
st = []
arr.sort()
for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]: continue
    for j in range(i, len(arr)):
        if j > i + 1 and arr[j] == arr[j-1]: continue
        k = j + 1
        l = len(arr) - 1
        while (k < l):
            sum = arr[i]
            sum += arr[j]
            sum += arr[k]
            sum += arr[l]
            if sum == target:
                st.append([arr[i], arr[j], arr[k], arr[l]])
                k += 1
                l -= 1

                while k < l and arr[k] == arr[k-1]:
                    k += 1
                
                while l > k and arr[l] == arr[l-1]:
                    l += 1
                     
            elif sum < target:
                k += 1
            elif sum > target:
                l -= 1

print(st)
