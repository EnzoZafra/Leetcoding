class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getIndex(char):
            return ord(char) - ord('a')
        
        anagramMap = collections.defaultdict(list)
        for string in strs:
            counter = [0 for _ in range(26)]
            for char in string:
                index = getIndex(char)
                counter[index] += 1
            
            key = ','.join([str(x) for x in counter])
            print(counter, key)
            anagramMap[key].append(string)
        
        out = []
        print(anagramMap)
        for key, item in anagramMap.items():
            out.append(item)
        
        return out
            
        
        