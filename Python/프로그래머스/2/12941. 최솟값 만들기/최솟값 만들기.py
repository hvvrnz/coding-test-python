def solution(A,B):
    total_1 = 0
    total_2 = 0
    
    a = sorted(A)
    rb = sorted(B, reverse=True)
    ra = sorted(A, reverse=True)
    b = sorted(B)
    
    for i in range(len(A)):
        total_1 += a[i] * rb[i]
        total_2 += ra[i] * b[i]
    
    return total_1 if total_1 < total_2 else total_2
        