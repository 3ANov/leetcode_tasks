class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums.count(val) != 0:
            nums.remove(val)



nums = [0,1,2,2,3,0,4,2]
# nums[nums.index(0):nums.count(0)-1] = []
# print(nums)
Solution().removeElement(nums, val=2)
print(nums)