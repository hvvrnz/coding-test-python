def solution(k, tangerine):
    remain = k
    d = {}
    count = 1
    
    for size in tangerine:
        if size in d:
            d[size] += 1
        else:
            d[size] = 1
            
    tangerine_list = [total for size, total in sorted(d.items(), key=lambda x: x[1], reverse=True)]
    
    for i in range(len(tangerine_list)):
        remain -= tangerine_list[i]
        if remain == 0:
            return count
        elif remain > 0:
            count += 1
        else:
            return count
            
        
        