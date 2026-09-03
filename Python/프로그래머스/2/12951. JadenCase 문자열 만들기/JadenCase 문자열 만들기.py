def solution(s):
    result = []
    start = True
    
    for ch in s:
        if ch == " ":
            result.append(ch)
            start = True
        elif start:
            result.append(ch.upper())
            start = False
        else:
            result.append(ch.lower())
            
    return "".join(result)