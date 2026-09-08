import math 

def solution(brown, yellow):
    area = brown + yellow
    
    for h in range(1, int(math.sqrt(area))+1):
        if area % h == 0:
            w = area // h
            if (w-2) * (h-2) == yellow:
                return [w, h]