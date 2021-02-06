class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # char in [0] comes before char in [1]
        graph = defaultdict(set)
        inDegrees = {c:0 for word in words for c in word}
        
        for word1, word2 in zip(words, words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        inDegrees[char2] += 1
                    break
            else:
                # If there is no difference, make sure len2 is longer (not a prefix)
                if len(word2) < len(word1):
                    return ''
                
        print(graph)
        print(inDegrees)
        
        # topological sort
        zeroInDegrees = deque()
        for key,value in inDegrees.items():
            if value == 0:
                zeroInDegrees.append(key)
        
        print(zeroInDegrees)
        out = []
        
        # zeroInDegrees is a queue now 
        while zeroInDegrees:
            curr = zeroInDegrees.popleft()
            out.append(curr)
            
            neighbors = graph.get(curr, set())
            
            for neighbor in neighbors:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    zeroInDegrees.append(neighbor)
        
        # not all letters are in the output, there was a cycle and no valid ordering
        if len(out) < len(inDegrees):
            return ''
        
        return ''.join(out)
                
            
        
                 
            