def solution(s):
    list_s = sorted(s.split(), key=int)
    result = min(list_s, key=int) + " " + max(list_s, key=int)
    return result