class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {x:i for i, x in enumerate(S)}
        print(last)
        
        out = []
        offset = 0
        lastSeenSubstring = 0
        for i, x in enumerate(S):
            lastSeen = last[x]
            lastSeenSubstring = max(lastSeenSubstring, lastSeen)
            if i == lastSeenSubstring:
                print(i,x,lastSeen)
                out.append(i - offset + 1)
                offset = i + 1
        
        return out
            
            