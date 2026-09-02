import math 

def solution(n):
    total = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            big = n // i
            if i == big:
                total += big
            else:
                total += i + big
    return total