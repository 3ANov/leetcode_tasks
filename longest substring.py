#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def unique_symbols(self, s):
        return len(set(list(s))) == len(s)


    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 1

        unique_sub_set = set()

        substr = s[i:j]
        len_substr = 0
        max_substr = ''
        while i <= len(s):
            while j <= len(s):
                if self.unique_symbols(substr):
                    unique_sub_set.add(substr)
                j += 1
                substr = s[i:j]
            i += 1
            j = i + 1
            substr = s[i:j]
        #print(max_substr)

        for k in unique_sub_set:
            if len_substr < len(k):
                len_substr = len(k)
        #print(k)
        #print(sorted(unique_sub_set, key=len, reverse=True))
        return len_substr



# x = "" #abc 3
# print(Solution().lengthOfLongestSubstring(x))
x = "abcabcbb" #abc 3
print(Solution().lengthOfLongestSubstring(x))
print(Solution().unique_symbols('abcd'))
x = "bbbbb" #b 1
print(Solution().lengthOfLongestSubstring(x))
print(Solution().unique_symbols(x))
x = "pwwkew" #wke 3
print(Solution().lengthOfLongestSubstring(x))
x = "abcdefg" #wke 3
print(Solution().lengthOfLongestSubstring(x))

with open('input.txt') as file:
    data = file.read()

print(Solution().lengthOfLongestSubstring(data))
