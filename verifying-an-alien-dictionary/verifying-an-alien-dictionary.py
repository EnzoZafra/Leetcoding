class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letterToIndex = {char:i for i, char in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            for k in range(min(len(word1), len(word2))):
                char1 = word1[k]
                char2 = word2[k]
                print(char1, char2)
                if char1 != char2:
                    if letterToIndex[char1] > letterToIndex[char2]:
                        return False
                    else: 
                        break
                        
            else:
                if len(word1) > len(word2):
                    return False
        
        return True