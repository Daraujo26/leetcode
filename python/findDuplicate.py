# 287. Find the Duplicate Number (Medium)
# Given an array of integers nums containing n + 1 integers where each integer is
# in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

nums = []

def findDuplicate(nums):
    h = {}
    for i in nums:
        if i not in h:
            h.update({i:1})
        else:
            return i
        
print(findDuplicate(nums))