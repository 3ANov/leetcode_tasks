#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique_char_set = set()
        unique_sub_str = set()
        i = 0
        while len(s) != 0:
            for ch in s:
                if ch not in unique_char_set:
                    unique_char_set.add(ch)
                else:
                    break
                i += 1
            unique_char_set.clear()
            unique_sub_str.add(s[:i])
            s = s[1:]
            i = 0
        max_length = 0
        for k in unique_sub_str:
            if max_length < len(k):
                max_length = len(k)

        return max_length




x = "dvdf"
print(Solution().lengthOfLongestSubstring(x))
x = "abcabcbb" #abc 3
print(Solution().lengthOfLongestSubstring(x))
x = "bbbbb" #b 1
print(Solution().lengthOfLongestSubstring(x))
x = "pwwkew" #wke 3
print(Solution().lengthOfLongestSubstring(x))
x = "abcdefg" #wke 3
print(Solution().lengthOfLongestSubstring(x))

with open('input.txt') as file:
    data = file.read()

print(Solution().lengthOfLongestSubstring(data))
string = data
unique_char_set = set()
unique_sub_str = set()
i = 0
while len(string) != 0:
    for ch in string:
        if ch not in unique_char_set:
            unique_char_set.add(ch)
        else:
            break
        i += 1
    unique_char_set.clear()
    unique_sub_str.add(string[:i])
    string = string[1:]
    i = 0





print(unique_char_set, i)
print(len(sorted(unique_sub_str, key=len, reverse=True)[0]), i)
print(string[:i])
