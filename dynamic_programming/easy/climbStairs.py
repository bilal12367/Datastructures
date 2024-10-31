

def climbStairs(n):
    if n <= 1:
        print("For n = ",n," returning 1")
        return 1
    
    l = climbStairs(n - 1)
    r = climbStairs(n - 2)
    print("For n = ",n , " l = ",l," r= ",r)
    return l + r
    
print(climbStairs(3))