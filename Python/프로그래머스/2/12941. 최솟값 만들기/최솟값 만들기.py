def solution(A,B):
    total = 0
    
    a = sorted(A)
    rb = sorted(B, reverse=True)
    
    for i in range(len(A)):
        total += a[i] * rb[i]
    
    return total
        