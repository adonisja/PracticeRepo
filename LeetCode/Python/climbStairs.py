def climbStairs(n):
    if n == 1 or n == 0:
        return 1
    return climbStairs(n-1)+ climbStairs(n-2)

def main():
    n = 5
    print(climbStairs(n))

if __name__ == '__main__':
    main()