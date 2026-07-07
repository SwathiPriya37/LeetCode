class Solution:
    def sumAndMultiply(self, n: int) -> int:
        addtion = 0
        n = str(n)
        res = ""

        for number in n:
            if number != "0":
                addtion += int(number)
                res += number
        
        if not res:
            return 0
        return int(res) * addtion