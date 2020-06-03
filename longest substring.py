#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 1
        substr = s[i:j]
        len_substr = 0
        max_substr = ''
        while i < len(s):
            while j < len(s):
                if substr in s[j:] and substr.count(substr[:1]) == 1:
                    if len_substr < len(substr):
                        len_substr = len(substr)
                        max_substr = substr
                j += 1
                substr = s[i:j]
            i += 1
            j = i + 1
            substr = s[i:j]
        print(max_substr)
        return len_substr




# x = "" #abc 3
# print(Solution().lengthOfLongestSubstring(x))
x = "abcabcbb" #abc 3
print(Solution().lengthOfLongestSubstring(x))
x = "bbbbb" #b 1
print(Solution().lengthOfLongestSubstring(x))
x = "pwwkew" #wke 3
print(Solution().lengthOfLongestSubstring(x))
x = "abcdefg" #wke 3
print(Solution().lengthOfLongestSubstring(x))