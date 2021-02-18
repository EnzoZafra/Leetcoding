class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return []
        
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1:
                countString = str(count)
                for c in countString:
                    chars[write] = c
                    write += 1
        
        return write