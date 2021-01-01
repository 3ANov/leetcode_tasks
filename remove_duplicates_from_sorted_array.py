class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            e_count = nums.count(i)
            el_index = nums.index(i)
            if e_count > 2:
                nums[el_index:el_index+e_count] = [i]
            if 1 < e_count <= 2:
                nums.remove(i)




nums = [-3,-1,0,0,0,3,3]
# nums[nums.index(0):nums.count(0)-1] = []
# print(nums)
Solution().removeDuplicates(nums)
print(nums)