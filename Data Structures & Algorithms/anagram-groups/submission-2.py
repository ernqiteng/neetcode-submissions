class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        words = {}
        for string in strs:
            sortedstring = ''.join(sorted(string))
            if sortedstring in words:
                curr_list = words[sortedstring]
                curr_list.append(string)
                words[sortedstring] = curr_list
            else:
                words[sortedstring] = [string]
        return list(words.values())