class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        """
        maxlen = 0
        left, right = 0, 0
        letters = set()
        currentstring = ""
        while right < len(s):
            print(s[right])
            currentstring = currentstring + s[right]
            print(currentstring)
            lenbefore = len(letters)
            letters.add(s[right])
            if len(letters) == lenbefore:
                #duplicate letter
                print("duplicate")
                left += 1
                currentstring = currentstring[1:]
            else: 
                maxlen = max(maxlen, len(currentstring))
            right += 1

        return maxlen
"""