class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        dp[0][0] = True
        
        # for an empty string, only a '*' will match
        for p_idx in range(1, len(p)+1):
            if p[p_idx-1] == '*':
                dp[0][p_idx] = dp[0][p_idx-1]
        
        for p_idx in range(1, len(p)+1):
            for s_idx in range(1, len(s)+1):
                
                # if we see a * 
                # 1. ignore the * and move to the next character in pattern
                # 2. OR * matches with the s_index character
                if p[p_idx-1] == '*':
                    dp[s_idx][p_idx] = dp[s_idx][p_idx-1] or dp[s_idx-1][p_idx]
                
                elif p[p_idx-1] == '?' or p[p_idx-1] == s[s_idx-1]:
                    dp[s_idx][p_idx] = dp[s_idx-1][p_idx-1]
                    
                else:
                    dp[s_idx][p_idx] = False
        
        return dp[-1][-1]
                    
                        
                        
                      
        
            