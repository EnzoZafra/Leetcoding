class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedStrings = {string : ''.join(sorted(string)) for string in strs}
        print(sortedStrings)
        
        groupAnagrams = collections.defaultdict(list)
        
        for string in strs:
            sortedString = sortedStrings[string]
            groupAnagrams[sortedString].append(string)
        
        return groupAnagrams.values()