class Codec:
    def __init__(self):
        self.empty = unichr(258)
        self.delimeter = unichr(257)

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return self.empty
        
        return unichr(257).join(x.encode('utf-8') for x in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == self.empty:
            return []
        
        return s.split((unichr(257)))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))