class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 0

        while low <= high :
            mid = low + (high - low) // 2
            temp = mid * mid

            if temp == x:
                return mid

            elif temp < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

            