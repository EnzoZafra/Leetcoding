class Solution(object):
    def isPalindrome(self, word):
        start = 0
        end = len(word) - 1
        
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
            
        return True
    
    def all_palindrome_prefixes(self, word):
        valid_prefixes = []
        for i in range(len(word)):
            # if the prefix is a palindrome
            if word[i:] == word[i:][::-1]:
                valid_prefixes.append(word[:i])
                
        return valid_prefixes
    
    def all_palindrome_suffixes(self, word):
        valid_prefixes = []
        for i in range(len(word)):
            # if the suffixes is a palindrome
            if word[:i+1] == word[:i+1][::-1]:
                valid_prefixes.append(word[i+1:])
                
        return valid_prefixes
            
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        wordSet = set(words)
        out = []
        
        for i in range(len(words)):
            word = words[i]
            wordReversed = word[::-1]
            
            # case 1
            if wordReversed in wordSet and i != words.index(wordReversed):
                out.append((i, words.index(wordReversed)))
        
            # case 2
            for suffix in self.all_palindrome_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in wordSet:
                    out.append((words.index(reversed_suffix), i))
                    
            # case 3
            for prefix in self.all_palindrome_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in wordSet:
                    out.append((i, words.index(reversed_prefix)))
        
        return out
        
        