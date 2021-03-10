class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        jobs = []
        
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        
        jobs.sort(key=lambda x:x[0])
        
        # dp[i] = max profit taking elements from the suffix starting at i
        dp = [0 for _ in range(n)]
        
        dp[-1] = jobs[-1][2]
        
        for i in range(n-2, -1, -1):
            next = self.findNext(i, jobs)
            
            add = 0 if next == -1 else dp[next]
            schedule_new = jobs[i][2] + add
            take_prev_job = dp[i+1]
            
            dp[i] = max(schedule_new, take_prev_job)
        
        return dp[0]
            
            
            
    def findNext(self, curr, jobs):
        for i in range(curr + 1, len(jobs)):
            if jobs[i][0] >= jobs[curr][1]:
                return i
        
        return -1
            