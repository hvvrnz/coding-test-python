import collections

def solution(k, tangerine):
    result = 0
    cnt = collections.Counter(tangerine)
    for i in sorted(cnt.values(), reverse=True):
        k -= i
        result += 1
        if k <= 0:
            return result