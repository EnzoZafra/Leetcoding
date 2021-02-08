class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.word = False
        self.children = [None for _ in range(26)]
    
    def getChildIndex(self, char):
        return ord(char) - ord('a')

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
    
    def printTrie(self):
        s = []
        s.append((self.root, ''))
        
        while s:
            curr, nodeString = s.pop()
            nodeString += curr.val
            if curr.word:
                print(nodeString)
            for child in curr.children:
                if child:
                    s.append((child, nodeString))

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root 
        for char in word:
            index = curr.getChildIndex(char)
            charNode = curr.children[index]
            
            if not charNode:
                charNode = TrieNode(char)
                curr.children[index] = charNode
            
            curr = charNode
        
        curr.word = True
    
    def search_recur(self, start, word):
        curr = start
        for i, char in enumerate(word):
            if char == '.':
                for child in curr.children:
                    if child:
                        test = self.search_recur(child, word[i+1:])
                        if test:
                            return True
                return False
            else:
                index = curr.getChildIndex(char)
                charNode = curr.children[index]

                if not charNode:
                    return False
                else:
                    curr = charNode
                    
        return curr.word
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_recur(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)