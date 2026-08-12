class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        n = len(s)
        i = 0
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            j = i
            while j < n and s[j] != ' ':
                j += 1
            s[i:j] = reversed(s[i:j])
            i = j
        return ' '.join(''.join(s).split())