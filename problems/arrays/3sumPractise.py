
nums = [-1, 0, 1, 2, -1, -4]


# k = ans - (i + j)
def sum3Zero(arr):
    res = []
    print(arr)
    for i in range(len(arr)):
        st = {}
        for j in range(i+1, len(arr)):
            st[arr[j]] = j
            print("=========================")
            print(st)
            temp = -arr[i] - arr[j]
            print(temp)
            print(res)
            if temp in st and st[temp] != j:
                res += [[arr[i], arr[j], arr[st[temp]]]]
    return res


print(sum3Zero(nums))
