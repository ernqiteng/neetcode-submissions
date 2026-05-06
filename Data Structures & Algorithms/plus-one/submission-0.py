class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num = num + str(n)
        num = int(num)
        num += 1
        newdigits = []
        for n in str(num):
            newdigits.append(n)
        return newdigits