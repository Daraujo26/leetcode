# 1. Two Sum (Easy)
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i == j:
                pass
            elif nums[i] + nums[j] == target:
                return [i, j]

# This is the O(n^2) solution, there is a faster O(nlog(n)) solutions as well

print(twoSum([2,7,11,15], 26))