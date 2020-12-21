#https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s) - 1):
            if roman_to_int_dict[s[i]] < roman_to_int_dict[s[i + 1]]:
                result = result - roman_to_int_dict[s[i]]
            elif roman_to_int_dict[s[i]] >= roman_to_int_dict[s[i + 1]]:
                result = result + roman_to_int_dict[s[i]]

        result = result + roman_to_int_dict[s[len(s) - 1]]
        return result


print('Результат: ' + str(Solution().romanToInt('MCMXCIV')))