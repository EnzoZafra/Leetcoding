class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = {}

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode('')
        self.count = {}
        self.curr_input = ''
        
        self._initialize_dictionary(sentences, times)
    
    def _initialize_dictionary(self, sentences, times):
        for i, sentence in enumerate(sentences):
            self._add_word(sentence)
            self.count[sentence] = times[i]
    
    def _add_word(self, word):
        curr = self.root
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                new_node = TrieNode(char)
                curr.children[char] = new_node
                curr = new_node
        
        curr.isWord = True
    
    def find_all_words_from(self, node, prefix):
        words = []
        stack = [(node, prefix)]
        
        while stack:
            curr_node, prefix = stack.pop()
            if node != curr_node:
                prefix += curr_node.val
            
            if curr_node.isWord:
                words.append(prefix)
            
            for child in curr_node.children:
                stack.append((curr_node.children[child], prefix))
                
        return words
    
    def filter_top_3(self, words):
        heap = []
        for word in words:
            count = self.count[word]
            heapq.heappush(heap, (-count, word))

        out = [] 
        for _ in range(3):
            if heap:
                out.append(heapq.heappop(heap)[1])             
        
        return out
    
    def search(self, prefix):
        curr = self.root
        
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return []
        
        all_words =  self.find_all_words_from(curr, prefix)
        return self.filter_top_3(all_words)
        

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.curr_input += c
            return self.search(self.curr_input)
        else:
            if self.curr_input in self.count:
                self.count[self.curr_input] += 1
            else:
                self.count[self.curr_input] = 1
                self._add_word(self.curr_input)
                
            self.curr_input = ''


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)