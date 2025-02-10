def solution(S):
    count = total = 0
    digits = []
    for i in range(9999):
        num = i
        while num > 0:
            digits[count] = num % 10
            num = num // 10
        
        if sum(digits) == S:
            total += 1
