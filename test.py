def findSum(arr, target):
    res = []
    seen = {}
    for i in range(len(arr)): # arr = [1,3,2,4,7,6,9]
        diff = target - arr[i]
        print(f'diff: {diff}')
        if diff in seen:
            res.append((diff, arr[i]))
        else:
            seen[arr[i]] = i
            print(seen)
    return res

def main():
    arr = [1,3,2,4,7,6,9]
    target = 10
    print(findSum(arr, target))

if __name__ == "__main__":
    main()