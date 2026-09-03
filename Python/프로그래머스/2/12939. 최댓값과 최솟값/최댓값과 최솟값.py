def solution(s):
    list_s = sorted(s.split(), key=int)
    s_min, s_max = list_s[0], list_s[len(list_s)-1]
    result = s_min + " " + s_max
    return result