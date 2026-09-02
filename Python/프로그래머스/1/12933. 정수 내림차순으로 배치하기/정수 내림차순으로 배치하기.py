def solution(n):
    s = str(n)
    d = {}
    result = ""
    
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    
    for key, value in sorted(d.items(), reverse = True):
        result += key * value
    
    return int(result)
 