class Solution(object):
    def getNeighbours(self, word, graph):
        neighbors = []
        for i in range(len(word)):
            wildcard = word[:i]  + "*" + word[i+1:]
            for neighbor in graph[wildcard]:
                if neighbor != word:
                    neighbors.append(neighbor)
        return neighbors
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        L = len(beginWord)
        
        # need to build a neighbors list
        # given a word, where in the wordList can we go?
        
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                wildcard = word[:i] + "*" + word[i+1:]
                graph[wildcard].append(word)
        
        queue = deque()
        queue.append((beginWord, 0))
        visited = set()
                     
        while queue:
            curr, count = queue.popleft()
            visited.add(curr)
            if curr == endWord:
                return count + 1
            
            neighbours = self.getNeighbours(curr, graph)
            for neighbor in neighbours:
                if neighbor not in visited:
                    queue.append((neighbor, count + 1))
        
        return 0
            