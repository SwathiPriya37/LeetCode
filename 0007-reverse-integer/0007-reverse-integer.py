class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        n = abs(x)

        ans = 0
        while n > 0:
            r = n % 10
            ans = ans * 10 + r
            n //= 10

        ans *= sign

        if ans < -(2**31) or ans > 2**31 - 1:
            return 0

        return ans