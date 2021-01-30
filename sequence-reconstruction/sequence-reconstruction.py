class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        
        values = {x for seq in seqs for x in seq}
        graph = {i:[] for i in values}
        inDegrees = {i:0 for i in values}

        for l in seqs:
            for i in range(len(l)-1):
                source = l[i]
                dest = l[i+1]

                inDegrees[dest] += 1
                graph[source].append(dest)

        s = []

        for (k, v) in inDegrees.items():
            if v == 0:
                s.append(k)

        out = []
        while s:
            if len(s) != 1:
                return False
            
            curr = s.pop()
            out.append(curr)
            neighbors = graph.get(curr, [])

            for neighbor in neighbors:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    s.append(neighbor)
                    
        return out == org and len(values) == len(out)
        