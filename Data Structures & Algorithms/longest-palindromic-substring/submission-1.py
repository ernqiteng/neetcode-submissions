class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        def update(l, r):
            nonlocal resLen
            nonlocal resIdx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length
            l, r = i, i
            update(l, r)

            # even length
            l, r = i, i + 1
            update(l, r)

        return s[resIdx : resIdx + resLen]