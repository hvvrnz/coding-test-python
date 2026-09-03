def solution(s):
    zero_count = 0
    total_count = 0
    
    while s != "1":
        zero_count += s.count("0")
        s = bin(s.count("1"))[2:]
        total_count += 1
        
    return [total_count, zero_count]