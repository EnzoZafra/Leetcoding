class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = [None for _ in range(26)]
        self.word = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
    
    def _char_to_index(self, char):
        ascii = ord(char) - ord('a')
        return ascii

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        i = 0
        curr = self.root
        while i < len(word):
            char = word[i]
            index = self._char_to_index(char)
            charNode = curr.children[index] 
            
            if not charNode:
                newNode = TrieNode(char)
                curr.children[index] = newNode
                charNode = newNode
            
            curr = charNode
            i += 1
        
        curr.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        curr = self.root
        while i < len(word):
            char = word[i] 
            index = self._char_to_index(char)
            charNode = curr.children[index]
            
            if not charNode:
                return False
            else:
                curr = charNode
                i += 1
        
        return curr.word
            

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        i = 0
        curr = self.root
        while i < len(prefix):
            char = prefix[i]
            index = self._char_to_index(char)
            charNode = curr.children[index]
            
            if not charNode:
                return False
            else:
                curr = charNode
                i += 1
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)