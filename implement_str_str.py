class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


haystack = "aaaaa"
needle = "bba"

print(Solution().strStr(haystack=haystack, needle=needle))