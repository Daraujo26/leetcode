# 169. Majority Element (Easy)
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

array = [3,3,4]

def majorityElement(nums):
    
    h = {}
    for i in nums:
        if i not in h:
            h.update({i:1})
        else:
            h.update({i:h.get(i)+1})
    return list(h.keys())[list(h.values()).index(max(h.values()))]
    

print(majorityElement(array))