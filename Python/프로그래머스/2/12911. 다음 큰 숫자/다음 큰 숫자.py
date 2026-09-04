def solution(n):
    num = n + 1
    target = bin(n)[2:].count("1")
    
    while bin(num)[2:].count("1") != target:
        num += 1
    
    return num