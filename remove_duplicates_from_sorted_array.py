class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            while nums.count(i) != 1:
                nums.remove(i)


nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)
print(nums)