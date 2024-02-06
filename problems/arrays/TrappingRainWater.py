

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trapOptimal1(arr):

    l = []
    r = []
    prev = arr[0]
    right = arr[-1]
    for i in range(len(arr)):
        if prev < arr[i]:
            prev = arr[i]
        rI = len(arr) - i - 1
        if right < arr[rI]:
            right = arr[rI]
        l.append(max(prev, arr[i]))
        r.insert(0, max(right, arr[rI]))

    water = 0
    for i in range(len(l)):
        min1 = min(l[i], r[i])
        water += min1 - arr[i]

    return water


def trapOptimal2(height):
    n = len(height)
    left = 0
    right = n-1
    res = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] > maxLeft:
                maxLeft = height[left]
            else:
                res += maxLeft - height[left]
            left += 1
        else:
            if height[right] > maxRight:
                maxRight = height[right]
            else:
                res += maxRight - height[right]
            right -= 1
    return res


print(trapOptimal2(arr))
