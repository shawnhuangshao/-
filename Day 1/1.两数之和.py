class Solution:
'''
循环遍历数组找出两数，复杂度 O(n2)
'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
        return []