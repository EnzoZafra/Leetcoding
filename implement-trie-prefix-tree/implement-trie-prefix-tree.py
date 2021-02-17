class TrieNode(object):
    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.isWord = False
    

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        ptr = 0 
        curr = self.root 
        while ptr < len(word):
            char = word[ptr] 
            if char in curr.children:
                curr = curr.children[char]
            else:
                newNode = TrieNode(char)
                curr.children[char] = newNode
                curr = newNode
            
            ptr += 1
                
        curr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = 0 
        curr = self.root 
        while ptr < len(word):
            char = word[ptr] 
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
            
            ptr += 1
                
        return curr.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = 0 
        curr = self.root 
        while ptr < len(prefix):
            char = prefix[ptr] 
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
            
            ptr += 1
                
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)