class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedstrs = []
        for i in range(len(strs)):
            sortedstrs.append(sorted(strs[i]))
        anagrams = []
        for i in range(len(sortedstrs)):
            if strs[i] != 0:
                matches = [strs[i]]
                for j in range(i+1, len(sortedstrs)):
                    if sortedstrs[j] == 0:
                        continue
                    elif sortedstrs[i] == sortedstrs[j]:
                        matches.append(strs[j])
                        strs[j] = 0
                anagrams.append(matches)
        return anagrams

        