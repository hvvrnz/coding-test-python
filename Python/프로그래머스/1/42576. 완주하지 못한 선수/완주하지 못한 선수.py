from collections import Counter

def solution(participant, completion):
    total_part =  Counter(participant)
    total_comp = Counter(completion)
    return list((total_part - total_comp).keys())[0]