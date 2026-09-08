def solution(nums):
    category = len(set(nums))
    return min(len(nums) // 2, category)