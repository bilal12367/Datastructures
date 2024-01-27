def myAtoi(s: str) -> int:
    nums = [str(i) for i in range(0, 10)] + ['-']
    str1 = ''
    print(nums)
    for i in s:
        if i in nums:
            str1 += i
    return int(str1)


print(myAtoi('   words    __-23'))
