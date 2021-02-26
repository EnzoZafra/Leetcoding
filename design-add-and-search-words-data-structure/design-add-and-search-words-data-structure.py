class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
    
    def _printTrie(self):
        print('printing trie')
        
        stack = [(self.root, '')]
        while stack:
            curr, stringSoFar = stack.pop()
            stringSoFar = stringSoFar + curr.val 
            if curr.isWord:
                print(stringSoFar)
            
            for child in curr.children:
                stack.append((curr.children[child], stringSoFar))

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        
        for char in word:
            if char in curr.children:
                node = curr.children[char]
            else:
                node = TrieNode(char)
                curr.children[char] = node
            
            curr = node
        curr.isWord = True
    
    def search_from_node(self, node, word):
        curr = node
        
        for i, char in enumerate(word):
            if char == '.':
                for child in curr.children:
                    if self.search_from_node(curr.children[child], word[i+1:]):
                        return True
                    
                return False
                
            elif char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        return curr.isWord
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.search_from_node(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)