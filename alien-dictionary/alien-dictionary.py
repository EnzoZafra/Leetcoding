class Solution(object):
    def find_first_diff_char(self, word1, word2):
        
        p1 = 0
        p2 = 0
        
        while p1 < len(word1) and p2 < len(word2):
            char1 = word1[p1] 
            char2 = word2[p2]
            
            if char1 != char2:
                return char1, char2
            else:
                p1 += 1
                p2 += 1
        
        return None, None
            
    def build_graph(self, words):
        if not words:
            return None
        
        graph = collections.defaultdict(list)
        prev_word = words[0]
        for word in words[1:]:
            char1, char2 = self.find_first_diff_char(prev_word, word)
            if char1 and char2:
                graph[char1].append(char2)
            elif len(prev_word) > len(word):
                # if there is no difference and the prev word is longer than the next word
                return -1
            
            prev_word = word
        return graph
        
    def get_zero_indegrees(self, nodes, graph):
        indegrees = {node:0 for node in nodes}
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        
        zeroInDegrees = []
        for node, indegree in indegrees.items():
            if indegree == 0:
                zeroInDegrees.append(node)
                
        return indegrees, zeroInDegrees
    
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # for each pair of words, find the first index where the characters differ
        # build graph character [before, after]
        # wrt vs wrf - > t and f since wrt came before wtf, -> [t, f]
        # [t, f], [w, e], [r, t], [e,r]
        
        # we can do a topological sort to get a sorted list 
        
        graph = self.build_graph(words)
        if graph == -1:
            return ''
        
        nodes = set([char for word in words for char in word])
        
        # find the node that we start with -> nodes with 0 indegrees
        indegrees, zeroInDegrees = self.get_zero_indegrees(nodes, graph)
        
        sortedOrder = []
        while zeroInDegrees:
            curr = zeroInDegrees.pop()
            sortedOrder.append(curr)
            
            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zeroInDegrees.append(neighbor)
        
        if len(sortedOrder) < len(nodes):
            return ""
        
        return ''.join(sortedOrder)