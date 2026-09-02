def solution(s):
    d = {}
    
    for ch in s.lower():
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
            
    total_p = d.get("p",0) 
    total_y = d.get("y",0)
    
    return total_p == total_y