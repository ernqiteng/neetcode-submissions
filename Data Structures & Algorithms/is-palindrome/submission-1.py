class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for char in s:
            if char.isalnum():
                t = t + char
        t = t.lower()
        print(t)
        if t == t[::-1]:
            print(t[::-1])
            return True
        return False