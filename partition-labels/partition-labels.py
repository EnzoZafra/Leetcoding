class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # preprocess the string, and calculate max(i) for each character
        # traverse string from left to right
        # as we go right, we get the max i of the characters in our current substring
        # if current i = max, then we have a partition
        
        farthest_seen = {char:i for i, char in enumerate(S)}
        print(farthest_seen)
        
        partitions = []
        maxSoFar = -1
        length = 0
        
        for i, char in enumerate(S):
            length += 1
            farthestForChar = farthest_seen[char]
            maxSoFar = max(farthestForChar, maxSoFar)
            
            if i == maxSoFar:
                partitions.append(length)
                maxSoFar = -1
                length = 0
        
        return partitions