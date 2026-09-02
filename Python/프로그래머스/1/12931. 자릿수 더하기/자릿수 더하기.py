def solution(n):
    total = 0
    for char in str(n):
        total += int(char)
    return total