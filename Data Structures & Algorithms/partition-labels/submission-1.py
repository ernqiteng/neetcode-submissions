class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        for index in range(len(s)):
            lastindex[s[index]] = index

        currindex, size, end = 0, 0, 0
        output = []
        for currindex in range(len(s)):
            size += 1
            end = max(end, lastindex[s[currindex]])

            if currindex == end:
                output.append(size)
                size = 0

        return output