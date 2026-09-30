class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0
        while pointer < len(s):
            length = ""
            while s[pointer] != "#":
                length = length + s[pointer]
                pointer += 1
            pointer += 1
            decoded.append(s[pointer:pointer+int(length)])
            pointer += int(length)
        return decoded