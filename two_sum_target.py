"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target"""


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(twoSum([1, 2, 3, 4, 5], 6))
