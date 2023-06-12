""" 
Given an array of integers nums and an integer target,return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
enumerate gives you both the value and the index
You can return the answer in any order.
"""
""" 
Solution Notes
Solution One:
Double for Loop => brute force O(n^2)

Solution Two:
Dictinary Storage=> O(n)

"""


class Solution_1(object):
    def twoSum(self, nums, target):
        """ 
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]


sln = Solution_1()
nums = [2, 7, 11, 15]
arr = sln.twoSum(nums, 9)
print(arr)


class Solution_2(object):
    def twoSum(self, nums, target):
        """ 
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return ([seen[target - num], i])
            elif num not in seen:
                seen[num] = i


sln = Solution_2()
nums = [2, 7, 11, 15]
arr = sln.twoSum(nums, 9)
print(arr)

# emulation: i=>index . num=> value
numbers = [45, 25, 65, 78, 78]
for i, num in enumerate(numbers):
    print(f"i: {i} ,num: {num}")
