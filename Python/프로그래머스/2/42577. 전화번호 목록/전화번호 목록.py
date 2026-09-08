def solution(phone_book):
    sorted_pb = sorted(phone_book)
    for i in range(1, len(sorted_pb)):
        if sorted_pb[i].startswith(sorted_pb[i-1]):
            return False
    return True