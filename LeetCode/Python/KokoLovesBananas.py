def minEatingSpeed(piles, h): 
    l, r = 1, max(piles)
    ans = r
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours +=math.ceil()

        if hours <= h:
            ans = min(ans,k)
            r = k - 1
        else:
            l = k + 1
        return ans

def main():
    print(minEatingSpeed(piles, k))

if __name__ == '__main__':
    