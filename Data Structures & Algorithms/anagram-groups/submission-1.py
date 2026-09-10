class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        use a dictionary
        sorting the word gives uniform answer
        iterate over strs
        key - sorted word, value - list of actual word
        return [dict.values()]
        """
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