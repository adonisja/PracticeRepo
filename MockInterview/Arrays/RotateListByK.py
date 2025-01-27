def rotateK(A, k):
    print(f'k = {k}\nA[-k:] = {A[-k:]}\nA[:-k] = {A[:-k]}')
    n = len(A)
    if k == 0 or n == 0:
        return A
    k = k % n
    return A[-k:] + A[:-k]

def test_rotateK():
    test_cases = [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
        ([], 3, []),
        ([1], 2, [1]),
        ([-1, -2, -3, -4, -5], 3, [-3, -4, -5, -1, -2])
    ]

    for i, (A, k, expected) in enumerate(test_cases):
        result = rotateK(A, k)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed\n")

if __name__ == '__main__':
    test_rotateK()

'''Write a function that rotates a list by k elements.
For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?'''