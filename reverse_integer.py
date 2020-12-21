class Solution(object):
    def reverse(self, x):
        result = 0
        z = abs(x)
        while z > 0:
            result = result * 10
            result += z % 10
            z = z // 10
        if x < 0:
            result = -result
        if (result <= -2 ** 31) or (result >= 2 ** 31 - 1):
            return 0
        return result


class Solution(object):
    def reverse(self, x):
        result = int(str(abs(x))[::-1])
        if (result <= -2 ** 31) or (result >= 2 ** 31 - 1):
            return 0
        if x < 0:
            result = -result
        return result


print(Solution().reverse(-150))
x = [3, 0, 4, 1]

print(sorted(x))
