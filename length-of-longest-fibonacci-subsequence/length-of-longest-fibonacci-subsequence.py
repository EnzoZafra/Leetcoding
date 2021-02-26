class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        indexMap = {x:i for i, x in enumerate(arr)}
        dp = [[2 for _ in range(len(arr))] for _ in range(len(arr))]
        ans = 0 
        
        for k in range(2, len(arr)):
            for j in xrange(k):
                i = indexMap.get(arr[k] - arr[j], -1)
                
                if 0 <= i < j:
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])
        return ans if ans >= 3 else 0