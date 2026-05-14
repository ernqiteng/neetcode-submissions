class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        def backtrack(index, output):
            if index == len(s):
                results.append(output[:])
                return
            
            for i in range(index+1, len(s)+1):
                substring = s[index:i]
                if substring == substring[::-1]:
                    output.append(substring)
                    backtrack(i, output)
                    output.pop()
        
        backtrack(0, [])
        return results
