

def housemaxLoot(hArr, n):
    if n < 0:
        return 0
    if n == 0:
        return hArr[0]

    return max(hArr[n] + housemaxLoot(hArr, n - 2), housemaxLoot(hArr, n - 1))


def housemaxLootDP(hArr, n):
    t = [0 for _ in range(n+1)]
    for i in range(n+1):
        if i < 0:
            t[i] = 0
        if i == 0:
            t[i] = hArr[0]

        t[i] = max(hArr[i] + t[i - 2], t[i - 1])

    return t[n]


if __name__ == '__main__':
    hval = [6, 7, 1, 3, 8, 2, 4]
    print(housemaxLootDP(hval, len(hval) - 1))
