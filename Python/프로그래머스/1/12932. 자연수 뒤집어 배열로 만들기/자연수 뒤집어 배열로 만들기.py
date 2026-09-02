def solution(n):
    arr = []
    s = str(n)
    reverse = s[::-1]
    
    for i in range(len(s)):
        arr.append(int(reverse[i]))
        
    return arr